import requests

'''Create a html file that Google would show when you want to search something. 
The html file would be downloaded on the same catalogue -- by Xi Yan'''
headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
exit_ = False
while not exit_:
    kw = input('Enter what you want to search on Google: ')
    param = {'q': kw}
    response = requests.get(url='https://www.google.ca/search', params=param, headers=headers)
    filename = './GoogleSearchEngine/download_pages/'+str(kw)+'.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(response.text)
    print('Successfully downloaded the html file')
    ans = input('Do you wanna continue searching? (Y/N) ')
    while (ans != 'Y') and (ans != 'N'):
        ans = input("Please enter 'Y' or 'N'\nDo you wanna continue searching? (Y/N) ")
    if ans == 'Y':
        continue
    else:
        exit_ = True
