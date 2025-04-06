import ee
service_account = ' hackaccino@swaoil.iam.gserviceaccount.com'
credentials = ee.ServiceAccountCredentials(service_account, 'C:\SWAYAMs\PROJ\AGRO_SPHERE\swaoil-9a2d2d61f006.json')
# Initialize the Earth Engine library with the service account credentials  
ee.Initialize(credentials)
