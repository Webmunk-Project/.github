# Replicate the Amazon study by standing up your own copy of the Webmunk infrastructure

If you'd like to replicate our Amazon study, there are three main technology components needed:

1. [An enrollment server](https://github.com/Webmunk-Project/Webmunk-Enrollment-App) for administering participants and study arms.

2. [A data collection server](https://github.com/Webmunk-Project/Webmunk-Django) for gathering data collected from the field.

3. [A web browser extension](https://github.com/Webmunk-Project/Webmunk-Extension) that resides on participants' machines and gathers data for the study.

Please refer to each of the components above for detailed instructions to build and set up each.

## Webmunk Amazon Rule Sets

The Webmunk enrollment server orchestrates the study by providing *rule sets* to the browser extension, which periodically polls the enrollment server for any updates for its configuration. 

Rule sets are simple JSON documents that configure the extension to implement a specific experimental or observational condition. In the Amazon study, we implemented the condition where the extension would hide a random set of Amazon-affiliated products and the same number of non-Amazon products on a given page with a rule set with the high-level structure:

```
{
  "filters": [
    ...
  ],
  "rules": [
    ...
  ],
  "additional-css": [
    ".webmunk-highlight-block-red { background-color: #FFCDD2 !important; }",
    ".webmunk-highlight-block { background-color: #E65100; }",
    ".webmunk-hide-block { display: none !important; }"
  ],
  "actions": {
    ...
  },
  "log-elements": [
    ...
  ],
  "description": [
    "Thank you for participating in this Study.",
    "If you have questions about the study or need technical support, please contact the study team using the email address provided in the survey."
  ],
  "pending-tasks-label": "Please complete these tasks.",
  "tasks": [
    ...
  ],
  "key": "Qhvrmhxp9spERvawGPLozqnPhYgKoYjfTJv2CPQVqyk=",
  "upload-url": "https://data.example.com/data/add-bundle.json",
  "enroll-url": "https://enroll.example.com/enroll/enroll.json",
  "uninstall-url": "https://enroll.example.com/enroll/uninstall?identifier=<IDENTIFIER>"
}
```

Each of the sections are described in detail below.

### `filters`

The `filters` potion of the document defined the areas of the web where the extension is active, and where it is not. Since this project studied activity on the Amazon e-commerce site, we employed the following filter definition:

```
"filters": [
  {
    "excludePaths": [
      "^/gp/buy/",
      "^/gp/video/"
    ],
    "hostEquals": "amazon.com"
  },
  {
    "excludePaths": [
      "^/gp/buy/",
      "^/gp/video/"
    ],
    "hostSuffix": ".amazon.com"
  },
  {
    "excludeHostSuffix": "aws.amazon.com"
  }
],
```

This activated the extension on hosts on the `amazon.com` domain, but excluded the `^/gp/buy/` path to avoid capturing participants' financial information accidentally, and the `^/gp/video/` path to avoid overloading our data collection system with content from Amazon's Prime video service. We also excluded hosts on Amazon's AWS domains, as a number of sites use resources like S3 hosted on those domains that are not relevant to the study.

### `rules`

The `rules` section defines the matching rules (expressed as jQuery selectors) that are used to tag elements on the page for the purpose of logging and manipulation. Each rule consists of a `match` condition that identifies specific DOM elements in the HTML page, and an action (such as `add-class` or `remove-class`). For example the most basic rule is

```
{
  "add-class": "webmunk-asin-item",
  "match": ":isAmazonProductItem('')"
}
```

This rule adds the `webmunk-asin-item` class to each element on the page that matches the `:isAmazonProductItem('')` jQuery selector (defined in [the Amazon module](https://github.com/Webmunk-Project/Webmunk-Amazon-Module)). This allowed us treat specific elements of the page as being about a single product.

A rule that identified an Amazon-affiliated item:

```
{
  'add-class': 'webmunk-targeted-brand',
  'match': '.s-result-item:has(.a-text-normal:contains("Amazon Basic"))'
}
```

Every Amazon Basic item that appeared on a search page would be tagged with the `webmunk-targeted-brand` class.

Sometimes, rules could be applied at more levels than desired, so a rule like this one only retained the `webmunk-targeted-brand` class on the most specific page elements, removing the class from any ancestor elements:

```
{
    "remove-class": "webmunk-targeted-brand",
    "match": ".webmunk-targeted-brand:has(.webmunk-targeted-brand)"
}
```

To implement our random hiding algorithm (hide the Amazon-affiliated elements, and hide the same number of non-Amazon products), we implemented a jQuery selector that would hide each DOM element tagged with the `webmunk-hide-block` class, and would *also* hide the same number of elements that matched the selectors following the first one:

```
{
  "add-class": "webmunk-hide-block",
  "match": ":webmunkRandomMirror(.webmunk-targeted-brand .s-result-item.webmunk-asin-item .a-carousel-card.webmunk-asin-item)"
}
```

(This implementation was so specfic to this particular study that [it was implemented within the extension itself](https://github.com/Webmunk-Project/Webmunk-Extension/blob/main/js/app/content-script.js#L32), instead of one of the Webmunk modules.)

This extension only required the basic `add-class` and `remove-class` actions, but other extensions can add more actions, such as this one used to swap items on a page:

```
{
  "swap": ".search-result-block-0",
  "with": ".search-result-last-block-0"
},
```

These actions are typically implemented on a per-extension basis, to support the specific experimental needs. (They will likely be extracted in the future into a Webmunk actions module to support reuse.)

### `additional-css`

This section supports the `rules` section by defining the appearance of tagged items using standard CSS styles:

```
"additional-css": [
  ".webmunk-highlight-block-red { background-color: #FFCDD2 !important; }",
  ".webmunk-highlight-block { background-color: #E65100; }",
  ".webmunk-hide-block { display: none !important; }"
]
```

Given that we cannot know the internal assumptions of each page and the elements it expects to find, applying a CSS `display: none` style is preferable to removing the DOM element out of the page altogether and creating unpredictable side-effects.

### `actions`

The `actions` portion of the rule set defined event listeners for particular actions that we we wished to log as  data points. The structure of the portion is a JSON object, where the key in the root of the object corresponds to a class (typically added in the `rules` section above).

For example, the items tagged with the `webmunk-asin-item` class may have the following actions defined:

```
"webmunk-asin-item": {
  "on-click": [
    "log-click"
  ],
  "on-hide": [
    "log-hidden"
  ],
  "on-show": [
    "log-visible"
  ]
}
```

This definition instructs the extension to log an event each time a tagged item is clicked (`log-click`), when it appers on the page (`log-visible`), and when it scrolls out of the browser's viewport (`log-hidden`). These events are used as the basis for measuring how participants interact with elements on the page.

In some cases, only particular elements may be of interest, and an `ancestors` list may be provided that only execute the action for elements that have ancestor elements that match:

```
"webmunk-button": {
  "on-click": [
    {
      "name": "log-click",
      "ancestors": [
        ".a-button-stack",
        ".a-carousel-row-inner"
      ]
    },
    {
      "name": "log-click",
      "ancestors": [
        ".a-modal-scroller"
      ]
    }
  ]
}
```

### `log-elements`

The `log-elements` section defines elements on the page that should be logged, independently of the prior `filters` and `rules` sections. This uses a simple filter syntax that defines which URLs to log, as well as the events to be logged. For example:

```
{
  "filters": {
    "urlMatches": "amazon.com/.*/dp/.*"
  },
  "load": [
    "body"
  ],
  "leave": [
    "body"
  ]
},
```

On Amazon product pages, this logs the full HTML `body` element both when the page is loaded and when the participant leaves it. This allowed us to capture a log of the product pages the study participants visited during the study.

This item...

```
"webmunk-asin-item": {
  "on-click": [
    "log-click"
  ],
  "on-hide": [
    "log-hidden"
  ],
  "on-show": [
    "log-visible"
  ]
},
```

... logged clicks to items tagged as Amazon product items. This duplicated some of the functionality of the `action` section, but provided a useful second source of data to validate the data collected in the `actions` configuration.

This item implemented the observer that tracked participants' scroll behavior on the page:

```
"__webmunk-scroll-bar": {
  "on-scroll": [
    "log-scroll"
  ]
}

```

### Remaining items

The following remaining items were used to customize the user interface of the extension, such as the `description` item, which provided the text on the screen when a participant opened the extension window:

```
"description": [
  "Thank you for participating in this Study.",
  "If you have questions about the study or need technical support, please contact the study team using the email address provided in the survey."
],
```

`pending-tasks-label` provided a customizable label for each participant's task list (populated by the enrollment server):

```
"pending-tasks-label": "Please complete these tasks."
```

This accompanied a `tasks` list that consisted of a list of task labels and URLs:

```
"tasks": [
  {
    "message": "Complete Survey",
    "url": "https://foo.qualtrics.com/jfe/form/ABC123?webmunk_id=MY_ID"
  },
]
```

And finally, the following URLs instructed the extension where it should request its configuration (`enroll-url`, described by this document), where it should upload data (`upload-url`), and what endpoint it should load when the extension was uninstalled to notify the study staff (`uninstall-url`).

```
"upload-url": "https://server-1.webmunk.org/data/add-bundle.json",
"enroll-url": "https://enroll.webmunk.org/enroll/enroll.json",
"uninstall-url": "https://enroll.webmunk.org/enroll/uninstall?identifier=<IDENTIFIER>"
```

### Dynamic updates

While a static rule set may be sufficient for the most simple studies, any non-trivial study will require dynamic elements that allow the system to customize each participant's rule set based on their participation. The most obvious example is assigning different experimental arms, but there are other aspects that also benefit from a dynamic approach, such as generating new `rules` items based on a centralized list (such as a list of known Amazon brand names). Or it may be useful to remind a particular user that they need to upload their order history by adding items to the `tasks` list.

The Webmunk enrollment server accomodates that need by allowing studies to implement their own specific configurations as a settings variable, defined in either the site's `settings.py` or `local_settings.py`.

The `tasks` section may be customized by [implementing the `WEBMUNK_UPDATE_TASKS` function](https://github.com/Webmunk-Project/Webmunk-Enrollment-App/blob/main/site_settings.py-template#L195). It takes a participant enrollment as its first argument and a pointer to the `ScheduledTask` model type that is used to schedule tasks within the enrollment server. Our implementation generated an initial set of tasks for new users, and added new tasks to their extension as older tasks were completed. In this function, we implemented an automatic uninstall task that was provided after the study was over. 

While `WEBMUNK_UPDATE_TASKS` only operated on the `tasks` portion of the rule set, the `WEBMUNK_UPDATE_ALL_RULE_SETS` function [was more expansive in generating new items in the `rules` and `log-elements` sections](https://github.com/Webmunk-Project/Webmunk-Enrollment-App/blob/main/site_settings.py-template#L494). This allowed us to use expansive lists of Amazon brand names to generate rules to tag `webmunk-targeted-brand` items and to implement some basic logging of visits to Amazon competitors (see the `WEBMUNK_LOG_DOMAINS` array).

Without these dynamic elements, maintaining consistent rule sets across study arms and server assignments would have quickly grown into an unmanageable task. (They are tricky enough to manage *with* these aids.) Since different studies will have different requirements, the decision to make these effectively site-specific settings variables gives future Webmunk users the latitude to take what we've provided and customize that to implement their own unique studies.

### Questions or comments?

If you have any questions or comments about this document, please reach out to [chris@audacious-software.com](mailto:chris@audacious-software.com) for assistance or clarification.

