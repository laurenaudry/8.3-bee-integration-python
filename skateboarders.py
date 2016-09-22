from bottle import route, run, static_file, get

@route('/')
def main():
    return '''
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>Powell Peralta Skateboards</title>
        <link rel="stylesheet" href="styles/main.css">
        <!-- Link for font i got on google fonts for page -->
        <link href='https://fonts.googleapis.com/css?family=Hind' rel='stylesheet' type='text/css'>
      </head>
      <body>
        <div class="center">
          <header>
            <a href="subscribe" class="subscribe">
              subscribe
            </a>
            <!--took me a while to figure out you needed to include file name its in  -->
            <a href="facebook.com">
              <img src="assets/facebook.png" alt="facebook logo link" class="facebook"/>
            </a>
            <a href="rss-feed">
              <img src="assets/RSS.png" alt="rss feed link" class="rss"/>
            </a>
            <a href="twitter.com">
              <img src="assets/twitter.png" alt="twitter logo link"  class="twitter"/>
            </a>
            <a href="youtube.com">
              <img src="assets/youtube.png" alt="youtube logo link" class="youtube" />
            </a>
            <nav>
              <a href="#news" class="nav-bar">
                sk8t news
              </a>
              <a href="#skateboarders" class="nav-bar">
                skateboarders
              </a>
              <a href="#boards" class="nav-bar">
                board design
              </a>
              <a href="#contact" class="nav-bar">
                contact us
              </a>
          </header>
          <!--multiple div's required to put logo image on top of photographer image -->
        <main class="carousel__container">
          <div class="carousel__background">
            <img src="assets/grid.png" alt="grid texture" class="grid_texture"/>
            <img src="assets/peralta-logo.png" alt="powell peralta logo skeleton coming out of ring with wings" class="logo-img"/>
          </div>
        </main>
        <!-- wasnt sure about the dots. assume inner dots are same set-up? -->
        <section class="carousel_buttons">
          <a href="carouselImage-1" class="carousel_button-link">
          <div class="carousel_buttons-circle">
          </div>
          </a>
          <a href="carouselImage-2" class="carousel_button-link">
          <div class="carousel_buttons-circle">
          </div>
          </a>
          <div class="carousel_buttons-circle">
          </div>
          </a>
         </section>
        <!-- Seriously feel self concious about how many div's are in this... -->
        <div class="grid__column">
         <article class="article">
           <h2 class="article_title">
             Tony Hawk foundation raises big money at celeb fundraiser.
           </h2>
           <time datetime="20131010" class="article_date">
             October 10, 2013
           </time>
           <p class="article_preview">
             It was just over 90 degrees in Los Angeles, but that didn't stop the throngs from coming out to celebrate the 10th annual Tony Hawk's Stand Up For Skateparks Benefit Presented by SLS Hotel & Casino Las Vegas on Saturday at the Green Acres Estate in Beverly Hills.
           </p>
           <a href="link-to-article-page" class="readMore">
            [ read more ]
           </a>
         </article>
       </div>
        <div class="grid__column">
         <article class="article">
           <h2 class="article_title">
             Rodney Mullen: Pop an ollie and innovate!
             (TED Talk)
           </h2>
           <time datetime="20130310" class="article_date">
             March 10, 2013
           </time>
           <p class="article_preview">
            The last thing Rodney Mullen, the godfather of street skating, wanted were competitive victories. In the exuberant talk he shares his love of the open skateboarding community and how the unique environments it plays in drive the creation of new tricks -- fostering...
           </p>
           <a href="link-to-article-page" class="readMore">
            [ read more ]
           </a>
         </article>
       </div>
        <div class="grid__column">
         <article class="article">
           <h2 class="article_title">
            ray barbee talks 'ban this'
           </h2>
           <time datetime="20161004" class="article_date">
             October 4, 2013
           </time>
           <p class="article_preview">
             Since filming is in full swing for the Vans video Adventures With Chris has taken the opportunity to sit some of the team down to look behind the skating of some of their earlier parts. Today we sit down with Ray Barbee, one of the smoothest guys to ever step on a skateboard and Chris' childhood idol...
           </p>
           <a href="link-to-article-page" class="readMore">
            [ read more ]
           </a>
         </article>
       </div>
       <!-- Literally just div's -->
       <section class="skater_images">
         <div class="imageContainer lance">
           <h3 class="heading">Lance Mountain</h3>
         </div>
         <div class="imageContainer rodney">
           <h3 class="heading">Rodney Mullen</h3>
         </div>
         <div class="imageContainer tommy">
           <h3 class="heading">Tommy Guerrero</h3>
         </div>
         <div class="imageContainer steve">
           <h3 class="heading">Steve Caballero</h3>
         </div>
         </section>
      <section class="skateboards">
        <img src="assets/sk8-1.png" alt="" class="skateboardPadding"/>
        <img src="assets/sk8-2.png" alt="" class="skateboardPadding"/>
        <img src="assets/sk8-3.png" alt="" class="skateboardPadding"/>
        <img src="assets/sk8-4.png" alt="" class="skateboardPadding"/>
        <img src="assets/sk8-5.png" alt="" class="skateboardPadding"/>
        <img src="assets/sk8-6.png" alt="" class="skateboardPadding"/>
        <img src="assets/sk8-7.png" alt="" class="skateboardPadding"/>
        <img src="assets/sk8-8.png" alt="" class="skateboardPadding"/>
        <img src="assets/sk8-9.png" alt="" class="skateboardPadding"/>
        <img src="assets/sk8-10.png" alt="" class="skateboardPadding"/>
      </section>
      <footer class="footer_box">
        <section class="contact_section">
          <h2 class="contact_header">
          Contact us for more information
          </h2>
          <p>Shabby chic letterpress jean shorts everyday carry vegan, paleo YOLO semiotics offal. Aesthetic freegan four dollar toast, occupy XOXO tofu raw denim organic next level four loko squid kombucha craft beer farm-to-table.Kitsch etsy meditation occupy, selfies forage salvia actually lomo lumbersexual flannel taxidermy VHS. Tumblr fingerstache.</p>
        </section>

     <!-- Legit feel like I have way to many div's on this html file for it to be right. -->
        <section class="submit">
          <form action="/url-for-where-info-goes" method="post" class="form">
            <div>
                <input class="name" name="firstname" type="text" placeholder="Name" required />
            </div>
            <div>
                <input type="email" class="email" name="user_mail"
                placeholder="Email"/>
            </div>
            <div>
                <textarea class="msg" name="user_message"
                placeholder="Your message"></textarea>
            </div>
            <div>
                <button type="submit" class="button">Submit</button>
            </div>
          </form>
        </section>
     </footer>
    </body>
    '''


@get('/styles/<filename:path>')
def styles(filename):
    return static_file(filename, root='./styles')

@get('/assets/<filename:path>')
def assets(filename):
    return static_file(filename, root='./assets')

run(host='localhost', port='8080', debug=True)
