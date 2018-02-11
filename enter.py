from python import python

@python.route('/enter')
def enter():
    user = {'nickname': 'Starting Point'}  # fake user
    return '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
  <form action="entertrade" method="post" name="entertrade">
    <h1>Enter Trade</h1>
    <p><input type="submit" value="Trade"></p>
   </form>
   <form action="enterwatch" method="post" name="enterwatch">
    <h1>Enter Watch</h1>
    <p><input type="submit" value="Watch"></p>
   </form>
  </body>
</html>
'''
