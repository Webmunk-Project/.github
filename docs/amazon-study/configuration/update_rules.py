# This Python code is part of the enrollment server's settings.py file 
# and adds additional tagging rules to all of the other rulesets.
# We implemented it as part of the settings, as the volume of additional 
# rules added would be tricky to manage if we made them part of the rules 
# themselves, in terms of keeping everything synchronized.
#
# The WEBMUNK_UPDATE_ALL_RULE_SETS function takes one of the base rule sets,
# parses the JSON and adds new rules before reserializing the rules and
# returning them to the extension.

WEBMUNK_LOG_DOMAINS = (
    'anthropologie.com',
    'apple.com',
    'barnesandnoble.com',
    'bathandbodyworks.com',
    'bestbuy.com',
    'bhphotovideo.com',
    'birchbox.com',
    'bodybuilding.com',
    'boxed.com',
    'chewy.com',
    'costco.com',
    'cvs.com',
    'dillards.com',
    'dollargeneral.com',
    'ebay.com',
    'etsy.com',
    'forever21.com',
    'gamestop.com',
    'gap.com',
    'gnc.com',
    'hm.com',
    'homedepot.com',
    'hsn.com',
    'iherb.com',
    'ikea.com',
    'warbyparker.com',
    'johnlewis.com',
    'kohls.com',
    'kroger.com',
    'lego.com',
    'lordandtaylor.com',
    'nyxcosmetics.com',
    'lowes.com',
    'macys.com',
    'microsoft.com',
    'neimanmarcus.com',
    'newegg.com',
    'nike.com',
    'nordstrom.com',
    'overstock.com',
    'qvc.com',
    'rakuten.com',
    'riteaid.com',
    'samsclub.com',
    'sephora.com',
    'shop.app',
    'staples.com',
    'target.com',
    'vitaminshoppe.com',
    'ulta.com',
    'urbanoutfitters.com',
    'victoriassecret.com',
    'walgreens.com',
    'walmart.com',
    'wayfair.com',
    'yoox.com',
    'zappos.com',
    'zulily.com',
    'shop.app',
)

WEBMUNK_TARGETED_BRANDS = (
    'Amazon Aware',
    'Amazon Basic Care',
    'Amazon Basics',
    'AmazonBasics',
    'Amazon Brand',
    'Amazon Collection',
    'Amazon Commercial',
    'AmazonCommercial',
    'Amazon Elements',
    'Amazon Essentials',
    'Featured from our brands',
    '206 Collective',
    'Amazing Baby',
    'Buttoned Down',
    'Cable Stitch',
    'Daily Ritual',
    'Goodthreads',
    'Isle Bay',
    'Lark & Ro',
    'Moon and Back by Hanna Andersson',
    'Mountain Falls',
    'P2N Peak Performance',
    'Pinzon',
    'Presto!',
    'Simple Joys by Carter\'s',
    'Solimo',
    'Spotted Zebra',
    # 'Fire TV', # CK Added
    # '10.Or',
    # '365 By Whole Foods Market',
    # '365 Every Day Value',
    # 'A For Awesome',
    # 'A Made For Kindle',
    # 'Afa',
    # 'Afa Authentic Food Artisan',
    # 'Afterthought',
    # 'Alexa',
    # 'Allegro',
    # 'Always Home',
    # 'Amazon Chime',
    # 'Amazon Dash',
    # 'Amazon Echo',
    # 'Amazon Edv',
    # 'Amazon English',
    # 'Amazon Game Studios',
    # 'Amazon Pharmacy',
    # 'Amazon Spheres',
    # 'Amazon Tap',
    # 'Amazon.Com',
    # 'Amazonfresh',
    # 'Arabella',
    # 'Arthur Harvey',
    # 'Azalea',
    # 'Be',
    # 'Belei',
    # 'Berry Chantilly',
    # 'Blink',
    # 'Bloom Street',
    # 'C/O',
    # 'Camp Moonlight',
    # 'Candy Island Confections',
    # 'Celebration Caffe',
    # 'Cheddar Chicks',
    # 'City Butcher',
    # 'Coastal Blue',
    # 'Common Casuals',
    # 'Common District',
    # 'Compass Road',
    # 'Cooper James',
    # 'Countdown To Zero',
    # 'Creative Galaxy',
    # 'D R',
    # 'Daisy Drive',
    # 'Dayana',
    # 'Denali',
    # 'Denim Bloom',
    # 'Due East Apparel',
    # 'Eero',
    # 'Fairfax',
    # 'Find.',
    # 'Fire',
    # 'Floodcraft Brewing Company',
    # 'Flying Ace',
    # 'Franklin & Freeman',
    # 'Fresh Fields',
    # 'Georgia Style W.B. Williams Brand Peach Salsa #1 Select',
    # 'Halo',
    # 'Happy Belly',
    # 'House Of Boho',
    # 'Hs House & Shields Clothing Company',
    # 'James & Erin',
    # 'Jump Club',
    # 'Kailee Athletics',
    # 'Kindle',
    # 'Kitzy',
    # 'League Of Outstanding Kids Look',
    # 'Lemon Label Paper Supply',
    # 'Lily Parker',
    # 'M X G',
    # 'Made For Amazon',
    # 'Madeline Kelly',
    # 'Mademark',
    # 'Mae',
    # 'Mia Noir',
    # 'Mint Lilac',
    # 'Movian',
    # 'Mr Beams',
    # 'Nature\'s Wonder',
    # 'Night Swim',
    # 'Ninja Squirrel',
    # 'Nod By Tuft&Needle',
    # 'Nupro',
    # 'Obsidian',
    # 'Ocean Blues',
    # 'One Wine',
    # 'Orchid Row',
    # 'Outerwear Index Co.',
    # 'Painted Heart',
    # 'Plumberry',
    # 'Ready When You Are',
    # 'Readyvolt',
    # 'Rebellion',
    # 'Replenish',
    # 'Ring',
    # 'Romantic Dreamers',
    # 'Scout + Ro',
    # 'Scuba Snacks',
    # 'Seeduction',
    # 'Sekoa',
    # 'Seriously Tasty',
    # 'Silly Apples',
    # 'Society New York',
    # 'Sprout Star',
    # 'Starkey Spring Water',
    # 'Strathwood',
    # 'Suite Alice',
    # 'The Establishment',
    # 'The Plus Project',
    # 'The Portland Plaid Co',
    # 'The Slumber Project',
    # 'Thirty Five Kent',
    # 'Toes In A Blanket',
    # 'Tovess',
    # 'Truity',
    # 'Vox',
    # 'Wag',
    # 'Weaczzy',
    # 'Wellspring',
    # 'Whole Foods',
    # 'Wickedly Prime',
    # 'Wonder Bound',
    # 'Wood Paper Company',
    # 'Yours Truly',
    # 'Zanie Kids',
    # 'Zappos',
    # 'Gabriella Rocha',
    # 'Bouquets',
    # 'Vigotti',
    # 'Type Z',
    # 'Lassen',
    # 'Fitzwell',
    # 'Rsvp',
    # 'Strathwood',
    # 'Care Of By Puma',
)

def WEBMUNK_UPDATE_ALL_RULE_SETS(payload):
    if ('log-elements' in payload['rules']) is False:
        payload['rules']['log-elements'] = []

    for domain in WEBMUNK_LOG_DOMAINS:
        domain_rule = {
            'filters': {
                'hostEquals': domain,
                'hostSuffix': '.%s' % domain
            },
            'load': ['title'],
            'leave': ['title']
        }

        payload['rules']['log-elements'].append(domain_rule)

    payload['rules']['rules'].insert(0, {
        'match': '.webmunk-targeted-brand .webmunk-targeted-brand',
        'remove-class': 'webmunk-targeted-brand'
    })

    brands = []

    for brand in WEBMUNK_TARGETED_BRANDS:
        brands.append(brand)

#        brand_rule = {
#            'add-class': 'webmunk-targeted-brand',
#            'match': '.s-result-item:has(*:webmunkContainsInsensitive("%s")):visible' % brand
#        }

#        payload['rules']['rules'].insert(0, brand_rule)

#        brand_rule = {
#            'add-class': 'webmunk-targeted-brand',
#            'match': '.s-result-item:has(.a-text-normal:contains("%s"))' % brand
#        }
#
#        payload['rules']['rules'].insert(0, brand_rule)
#
#        brand_rule = {
#            'add-class': 'webmunk-targeted-brand',
#            'match': '.s-result-item:has(.a-color-base:contains("%s"))' % brand
#        }
#
#        payload['rules']['rules'].insert(0, brand_rule)
#
#        brand_rule = {
#            'add-class': 'webmunk-targeted-brand',
#            'match': '.s-result-item:has(.s-light-weight-text:contains("%s"))' % brand
#        }
#
#        payload['rules']['rules'].insert(0, brand_rule)

#        brand_rule = {
#            'add-class': 'webmunk-targeted-brand',
#            'match': '.s-inner-result-item:has(*:webmunkContainsInsensitive("%s")):visible' % brand
#        }
#
#        payload['rules']['rules'].insert(0, brand_rule)

#        brand_rule = {
#            'add-class': 'webmunk-targeted-brand',
#            'match': '.s-inner-result-item:has(.a-text-normal:contains("%s"))' % brand
#        }
#
#        payload['rules']['rules'].insert(0, brand_rule)
#
#        brand_rule = {
#            'add-class': 'webmunk-targeted-brand',
#            'match': '.s-inner-result-item:has(.a-color-base:contains("%s"))' % brand
#        }
#
#        payload['rules']['rules'].insert(0, brand_rule)
#
#        brand_rule = {
#            'add-class': 'webmunk-targeted-brand',
#            'match': '.s-inner-result-item:has(.s-light-weight-text:contains("%s"))' % brand
#        }
#
#        payload['rules']['rules'].insert(0, brand_rule)

    brand_rule = {
        'add-class': 'webmunk-targeted-brand',
        'match': '.s-result-item:has(*:webmunkContainsInsensitiveAny(%s)):visible' % json.dumps(brands)
    }

    payload['rules']['rules'].insert(0, brand_rule)

    brand_rule = {
        'add-class': 'webmunk-targeted-brand',
        'match': '.s-result-item:has(*:webmunkContainsInsensitiveAny(%s)):visible' % json.dumps(brands)
    }

    payload['rules']['rules'].insert(0, brand_rule)

    brand_rule = {
        'add-class': 'webmunk-targeted-brand',
        'match': '.s-inner-result-item:has(*:webmunkContainsInsensitiveAny(%s)):visible' % json.dumps(brands)
    }

    payload['rules']['rules'].insert(0, brand_rule)

    brand_rule = {
        'add-class': 'webmunk-targeted-brand',
        'match': '.a-carousel-card:not(:has([data-video-url])):visible:has(*:webmunkContainsInsensitiveAny(%s))' % json.dumps(brands)
    }

    payload['rules']['rules'].insert(0, brand_rule)

    brand_rule = {
        'remove-class': 'webmunk-targeted-brand',
        'match': '.a-carousel-card:not(:has([data-video-url])):visible:not(:has(*:webmunkContainsInsensitiveAny(%s)))' % json.dumps(brands)
    }

    payload['rules']['rules'].insert(0, brand_rule)

    brand_rule = {
        'add-class': 'webmunk-targeted-brand',
        'match': '#value-pick-ac:has(*:webmunkContainsInsensitiveAny(%s)):not(:has([data-video-url])):visible' % json.dumps(brands)
    }

    payload['rules']['rules'].insert(0, brand_rule)

    brand_rule = {
        'add-class': 'webmunk-targeted-brand',
        'match': '.webmunk-asin-item:visible:has(*:webmunkContainsInsensitiveAny(%s))' % json.dumps(brands)
    }

    payload['rules']['rules'].insert(0, brand_rule)

    brand_rule = {
        'add-class': 'webmunk-targeted-brand',
        'match': '.webmunk-asin-item:visible:has(*:webmunkImageAltTagContainsInsensitiveAny(%s))' % json.dumps(brands)
    }

    payload['rules']['rules'].insert(0, brand_rule)
