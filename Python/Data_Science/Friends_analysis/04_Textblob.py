from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the provided text.
    
    Args:
    text (str): The text to analyze.
    
    Returns:
    sentiment (str): The sentiment of the text (positive, neutral, or negative).
    polarity (float): The polarity score of the text (-1 to 1).
    """
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the sentiment polarity
    polarity = blob.sentiment.polarity
    
    # Determine sentiment category
    if polarity > 0:
        sentiment = 'positive'
    elif polarity == 0:
        sentiment = 'neutral'
    else:
        sentiment = 'negative'
    
    return sentiment, polarity

# Example text (you can replace this with any long text)
text = """
Finally, something Gerald Genta didn't design. As it turns out, when you're a guy as prolific as Genta, who pumped out hundreds of designs for 15 francs a pop in the '50s and '60s, you get credit for even the stuff you didn't do. But Audemars Piguet is unequivocal in who designed the "Disco Volante" ref. 5093...

Audemars Piguet sometimes also worked with independent designers, such as the German Gebhard Duve, who created the so-called 'Discovolante' 5093 models in the 1950s," it writes on its excellent AP Chronicles site. AP also provides these 1952 sketches from Duve:

Oh man, I love a good archival sketch. A 1952 sketch from designer Gebhard Duve, presented to Jacques Louis Audemars. One of these would lead to the Ref. 5093 "Disco Volante." Image: Courtesy of AP Chronicles

Somewhere along the way, history got muddled, and now Genta often gets the credit. Even I parrotted it a few days ago on social media, so a huge thanks to Jeff Stein (more than a Heuer guy!) for alerting me to the error of my ways.

Duve sketched out the above design in the 1950s and showed it to Jacques Louis Audemars, the grandson of one of AP's founders who ran creative for the brand, and it eventually became the ref. 5093 "Disco Volante," or flying saucer in Italian. As others have nicely documented, the Disco Volante's roots are firmly Art Deco with Omega, Vacheron, and others making saucer-shaped cases, but Duve's 1950s spin refined the idea and pulled it firmly into the world of midcentury design.

The 5093 seems to have been produced in modest numbers from the '50s through the '70s. It measures 36mm and has no lugs. You can find it with any number of dial and bezel combos, in white or yellow gold or (more rare) platinum. I was able to spend some time with the yellow gold Disco Volante you see here that sold at Hindman Auctions just yesterday for $8,255.

It was the first time I'd spent any meaningful time with an AP Disco Volante, a watch I'd always found curious. First, I didn't realize how thin these things were – the case is about 3mm (add another couple millimeters for the crystal) and feels particularly thin against that wide bezel. This particular Disco Volante has a crosshatched pattern on the bezel with a Clous de Paris guilloche on the outer edge. It's a bit old man-y, like a Patek 3919 or 6119, but a little more out there, kind of like if your old man had a penchant for eating grilled cheese sammies at Grateful Dead shows in the '60s (would you believe this describes my 8th-grade theology teacher at my very Catholic middle school?).

It doesn't stop with the case shape: the strap is actually screwed and integrated right into the case, underneath the caseback. It accentuates the case's thinness and round shape. It probably makes swapping (or even finding) alternative straps a real pain in the ass, so go complain about quick-release spring bars and bracelets in an article about some fancy new watch. You'll also find some 5093s with gorgeous integrated bracelets.

Many Disco Volantes have Gubelin-signed dials for the retailer based in Lucerne, Switzerland. Beyond that, this one's a pretty simple crosshair design. It obviously has some blemishes, but that's to be expected for a '70s dress watch and pretty common for the 5093.

My favorite dial design found on the Disco Volante is the multi-tone with golden outer tracks that absolutely shimmer. While the above dial can land a little flat, these multi-tone ones are full of depth. Collector Alexandre Tritz (who also happens to make straps for Rexhepi) has one of the most gorgeous examples I've seen, and he was gracious enough to provide some photos for your enjoyment:

The reference 5093 from Audemars Piguet is part of these watches that I love, but I can't really tell why," Tritz said when I asked him about his love for the reference. "The balance between sophistication and simplicity is right here. A great collector once told me: 'It's quite easy to make a simple watch look complicated, but it's very hard to make a complicated watch look simple.' The Disco Volante perfectly illustrates this.

Beyond the simple and the two-tone, you'll find all kinds of bezel and dial designs on the Disco Volante. Take your pick – it's mostly a matter of taste; just go easy if you're gonna tell me I'm wrong.

Inside the Disco Volante is AP's ultra-thin caliber 2003, a manual movement measuring just 1.64mm thick. Designed in collaboration with LeCoultre and Vacheron, it was the thinnest caliber when introduced in the '40s (take that, F. Piguet 21!).

I've beaten the whole "AP is shapes, and not just that famous octagon" thing to death already this year, so I'm not going to belabor the point – read here or here if you want more. That said, the Disco Volante is one of the more out there ones and produced in larger numbers than truly weird stuff like that asymmetrical brute it calls the [Re]Master02. If AP's association with the vagary of "pop culture" is what sets it apart today, it's this combination of design and real watchmaking that defined AP in the mid-20th century.

Prices can vary widely, in part because there's so much variety for the single reference. Last month, a yellow-gold Disco Volante with one of those two-tone dials sold for $16,000 at an Italian auction. Like the Hindman example, the dial wasn't perfect, but nice enough (btw, don't think we don't see you photoshopping the blemishes off that dial in the cover image, Italian auction house – link here if you wanna see what I mean). The boys at Amsterdam Vintage Watches offered a white gold Disco Volante on a bracelet for €25,000 in 2022. You won't find a combo much better than this unless you come across a completely clean dial, so let's call that the top of the market. Meanwhile, rattier examples have sold for as low as a few thousand bucks. 

The Disco Volante at Hindman is more of an average result, but the multiple bidders do indicate strong interest for the reference. Perhaps it's part of the whole "people like smaller, dressier, design-driven watches now" that's spawned a million think pieces and even more Hodinkee Radio conversations. 

The Disco Volante might even be having a bit of a moment, with Furlan Marri releasing its take on the flying saucer just last week. But I don't want to get into the meta of it all. It's just a cool shape that I find utterly fascinating. 

So here's to you and your groovy disco volante, Gebhard Duve.

Thanks to Hindman Auctions and Reginald Brack for letting me photograph this flying saucer.
"""

# Analyze sentiment
sentiment, polarity = analyze_sentiment(text)

print(f"Sentiment: {sentiment}")
print(f"Polarity: {polarity}")
