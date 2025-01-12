document.getElementById("switch").addEventListener("click", function() {
  var textElement = document.getElementById("sumexp"); // old text
  var ai = 0;
  textElement.textContent = "The colorful, spiky stars are in the foreground of this image taken with a small telescope on planet Earth. They lie well within our own Milky Way Galaxy. But the two eye-catching galaxies in the frame lie far beyond the Milky Way, at a distance of over 300 million light-years. The galaxies' twisted and distorted appearance is due to mutual gravitational tides as the pair engage in close encounters. Cataloged as Arp 273 (also as UGC 1810), these galaxies do look peculiar, but interacting galaxies are now understood to be common in the universe. Closer to home, the large spiral Andromeda Galaxy is known to be some 2 million light-years away and inexorably approaching the Milky Way.  In fact the far away peculiar galaxies of Arp 273 may offer an analog of the far future encounter of Andromeda and Milky Way. Repeated galaxy encounters on a cosmic timescale ultimately result in a merger into a single galaxy of stars. From our perspective, the bright cores of the Arp 273 galaxies are separated by only a little over 100,000 light-years. (Original)"; // new text
});

document.getElementById("switchback").addEventListener("click", function() {
  var textElement = document.getElementById("sumexp");// old text
  var ai = 1;
  textElement.textContent = "The image shows two interacting galaxies (Arp 273), over 300 million light-years away, exhibiting distorted shapes due to their gravitational pull on each other.  These galaxies, visible even with a small telescope, offer a glimpse into how galaxies interact and eventually merge.  The foreground stars, much closer within our Milky Way, appear spiky due to atmospheric effects in the Earth-based telescope image. (AI Summarized)"; // new text
});