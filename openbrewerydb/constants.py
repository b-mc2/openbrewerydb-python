
base_url = 'https://api.openbrewerydb.org/breweries'

states = {'alabama',
          'alaska',
          'arizona',
          'arkansas',
          'california',
          'colorado',
          'connecticut',
          'delaware',
          'district of columbia',
          'florida',
          'georgia',
          'hawaii',
          'idaho',
          'illinois',
          'indiana',
          'iowa',
          'kansas',
          'kentucky',
          'louisiana',
          'maine',
          'maryland',
          'massachusetts',
          'michigan',
          'minnesota',
          'mississippi',
          'missouri',
          'montana',
          'nebraska',
          'nevada',
          'new hampshire',
          'new jersey',
          'new mexico',
          'new york',
          'north carolina',
          'north dakota',
          'ohio',
          'oklahoma',
          'oregon',
          'pennsylvania',
          'rhode island',
          'south carolina',
          'south dakota',
          'tennessee',
          'texas',
          'utah',
          'vermont',
          'virginia',
          'washington',
          'west virginia',
          'wisconsin',
          'wyoming',
          }

brewery_types = {'micro',
                 'nano',
                 'regional',
                 'brewpub',
                 'large',
                 'planning',
                 'bar',
                 'contract',
                 'proprietor',
                 }

dtypes = {'id': int,
          'brewery_type': 'category',
          'state': 'category',
          'country': 'category',
          'latitude': float,
          'longitude': float,
          }
