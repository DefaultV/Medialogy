<?php
session_start();
$m = new MongoClient();

echo "Connected!";
$db = $m->mydb;

echo "Database mydb";
?>

<html>
  <head><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>Jdrews - Portfolio</title>
    <link rel="stylesheet" href="style.css">
    <link rel="icon" href="favicon.ico?v=2" />
  </head>

  <body>
      <video autoplay muted loop id="Video">
        <source src="projects/img/vid_f2.mp4" type="video/mp4">
        </video>
				
  <div class="title"><img src="projects/img/title.png"></img>
</div>
  <div class="section" id="s2"><h1 class="txt_overlay"><p>Ebb<br><i>WIP / <a id="pag" href="projects/ebb.php">More</a></i></p></h1>
    <div class="content" id="c2"></div>
  </div>
  <div class="section" id="s1"><h1 class="txt_overlay"><p>Picnic TD<br>
<i><a id="pag" href="projects/downloads/picnic.zip">Download
</a>
/ 
<a id="pag" href="projects/picnic.php">More</a>
</i></p></h1>
    <div class="content" id="c1"></div>
  </div>
		<div class="section" id="s6">
		    <h1 class="txt_overlay">
		        <p>CUBI<br>
		        <i><a id="pag" href="https://play.google.com/store/apps/details?id=com.Company.JaGaGames">Playstore
		        </a> / <a id="pag" href="projects/geogap.php">More</a></i></p></h1>
    <div class="content" id="c6"></div>
  </div>
  <div class="section" id="s4"><h1 class="txt_overlay"><p>Voidmaker<br><i>On hold / <a id="pag" href="projects/voidmaker.php">More</a></i></p></h1>
    <div class="content" id="c4"></div>
  </div>
  <div class="section" id="s3"><h1 class="txt_overlay"><p>Iso<br><i>On hold / <a id="pag" href="projects/iso.php">More</a></i></p></h1>
    <div class="content" id="c3"></div>
  </div>
  <div class="section" id="s5"><h1 class="txt_overlay"><p>SpaceCrusade<br><i><a id="pag" href="projects/downloads/spacecrusade.zip">Download</a> / <a id="pag" href="projects/spacecrusade.php">More</a></i></p></h1>
    <div class="content" id="c5"></div>
  </div>

  </body>
</html>

