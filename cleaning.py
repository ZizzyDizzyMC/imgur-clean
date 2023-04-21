import re
f = open("unclean_url_source", "r")
dump = f.read()
f.close()
horribleidea = re.findall(r"(?:(?:(?:https?:\\?\/\\?\/)?(?:www\.|[im]\.)?imgur(?:\.|(?:.?dot.?)|.)?(?:com|io)(?:\\\/|\\|\/|.?slash|(?:.?slash|.?\/)(?:\w|[^\S\r\n]|%2F)))?,(?:(?!gallery|search)(?:r\/\w+\/)?(\w{7}|\w{5})[bghlmrst]?)|(?:(?:https?:\\?\/\\?\/)?(?:www\.|[im]\.)?(?:i\.stack\.)imgur(?:\.|(?:.?dot.?)|.)?(?:com|io)\\?\/?)(?:(?!gallery|search)(?:r\/\w+\/)?(\w{7}|\w{5})[bghlmrst]?)|(?:(?:https?:\\?\/\\?\/)?(?:www\.|[im]\.)?(?<!(?:i\.stack\.))imgur(?:\.|(?:.?dot.?)|.)?(?:com|io)(?:\\\/|\\|\/|.?slash|(?:.?slash|.?\/)(?:\w|[^\S\r\n])|%2F))(?:(?!gallery|search)(?:r\/\w+\/)?(?:(?:original|mp4)(?:\\\/|\\|\/|.?slash|(?:.?slash|.?\/)(?:\w|[^\S\r\n])|%2F).+?|download(?:\\\/|\\|\/|.?slash|(?:.?slash|.?\/)(?:\w|[^\S\r\n])|%2F)?)?(\w{7}|\w{5})[bghlmrst]?|(?:a\/?\\?(\w{7}|\w{5}))|(?:(?:gallery|t\/\w+)\/(\w{7}|\w{5}))|(?:(?:user\/([^\/?#]+)(?:\", )+?(?:\/posts|\/submitted)?\/?)|(?:user\/([^\/?#]+)(?:\/posts|\/submitted)\/?)|(?:user\/([^\/?#]+)(?:\/favorites)\/?))))", dump)
with open('links.txt', 'a') as f:
  for i in range(len(horribleidea)):
    current = horribleidea[i]
    if current[0]:
      print('https://imgur.com/' + current[0])
      f.write('https://imgur.com/' + current[0] + '\n')
    if current[1]:
      print('https://i.stack.imgur.com/' + current[1] + '.png')
      f.write('https://i.stack.imgur.com/' + current[1] + '.png' + '\n')
    if current[2]:
      print('https://imgur.com/' + current[2])
      f.write('https://imgur.com/' + current[2] + '\n')
    if current[3]:
      print('https://imgur.com/a/' + current[3])
      f.write('https://imgur.com/a/' + current[3] + '\n')
    if current[4]:
      print('https://imgur.com/gallery/' + current[4])
      f.write('https://imgur.com/gallery/' + current[4] + '\n')
    if current[5]:
      print('https://imgur.com/user/' + current[5])
      f.write('https://imgur.com/user/' + current[5] + '\n')
    if current[6]:
      print('https://imgur.com/user/' + current[6]+ '/posts')
      f.write('https://imgur.com/user/' + current[6]+ '/posts' + '\n')
    if current[7]:
      print('https://imgur.com/user/' + current[7]+ '/favorites')
      f.write('https://imgur.com/user/' + current[7]+ '/favorites' + '\n')
print("Complete")
