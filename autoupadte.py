import requests
import json
import urllib.request


# this is the api url from transitfeeds(need api key)
data_url = "https://api.transitfeeds.com/v1/getFeeds?key=53c56515-36e5-4f1b-95b2-112eb4bcf40c&location=46&descendants=1&page=1&limit=22&type=gtfs"

# using requests, get a response from the web
response = requests.get(data_url)

if response:
    print('Success!')

    # access the data, we need json to load the response's content
    data_dict = json.loads(response.content)

    # based on the structure of the JSON data, we are able to retreive the ids
    # for different location
    download_list = []  # initialize a download list
    for i in range(0, len(data_dict['results']['feeds'])):
        id = data_dict['results']['feeds'][i]['id']
        fn = data_dict['results']['feeds'][i]['t']
        # due to the link format, we need to change the id found a bit
        id = id.replace("/", "%2F")
        # we want to delete the "space" in the file names
        fn = fn.replace(" ", "")
        fn = fn.replace("/", "")
        fn = fn.replace("GTFS","")
        # create downloadable link for each gtfs file
        dlink = "https://api.transitfeeds.com/v1/getLatestFeedVersion?key=53c56515-36e5-4f1b-95b2-112eb4bcf40c&feed=" + id

        # append the download list
        download_list.append([dlink, fn])

    # now, download the files
    for i in range(0, len(download_list)):

        # HERE IMPORTANT: you need to change the filename(path)
        # so that the files will be downloaded into the dir you desired
        urllib.request.urlretrieve(download_list[i][0], filename="/Users/skyho/Desktop/hello/"+download_list[i][1]+"_gtfs.zip")
        
    print("Update Completed")
# if no response
else:
    print('An error has occurred.')
