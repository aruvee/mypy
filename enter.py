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
   <form action="entergann" method="post" name="entergann">
    <h1>Enter Gann</h1>
    <p><input type="submit" value="Gann"></p>
   </form>
   <form action="entergannpop" method="post" name="entergannpop">
    <h1>Gann POP</h1>
    <p><input type="submit" value="Gann POP"></p>
   </form>
  </body>
</html>
'''
