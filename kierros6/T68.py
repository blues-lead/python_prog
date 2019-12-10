# All functions, besides "read_input" and "break_text" function in "chain", i.e. current function calls next function
# Such the chain is performed in order to break the task and control phases of task.
# Program shrinks the text fed by user to known length of row and fills with whitespaces
#

def read_input():
    """Function reads user`s input while blank line not feeded
    :return list of rows user feeded"""
    text = []
    while True:
        txt = input()
        if txt == "":
            return text
        text.append(txt)


def break_text(txt,length):
    """
    Function brakes list of rows into list of words
    :param txt: Text feeded by user as a list
    :param length: length of shrinked row
    :return: return text as a list, where each row is shrinked and filled with whitespaes
    """
    cropped_list = []
    for i in txt:
        temp = i.split(" ")
        for j in temp:
            cropped_list.append(j)
    return rearrange_text(cropped_list,length)

def rearrange_text(br_text, length):
    """
    Function is called by "break_text()". Function reconfigure the text such, that
    each row is less than or equal to "length"
    :param br_text:
    :param length:
    :return: calls next function (fill_with_blanks)
    """
    line = ""
    lst = []
    for i in range(0,len(br_text)):
        if br_text[i] == "":
            continue
        if len(line) + len(br_text[i]) <= length:
            line +=br_text[i] + " "
        else:
            lst.append(line.strip())
            line = br_text[i] + " "
    lst.append(line)
    return fill_with_blanks(lst,length)

def fill_with_blanks(txt, length):
    """
    Function fills each row of the text with blank to meet length condition of each row
    :param txt: result of function "rearrange_text()". Text where each row is less than or equal to @length as a list
    :param length: given length of row
    :return: list of text filled with whitespaces where each row is equal to @length as a list
    """
    new_blanks = 0
    r_text = []
    for phrase in txt:
        inds = phrase.count(" ")
        # ===========================
        if len(phrase) < length and phrase != txt[-1]:
            new_blanks = length - len(phrase)
            if new_blanks <= inds:
                new_row = ""
                words = phrase.split(" ")
                z = 0
                blank = "  "
                for wrd in words:
                    if z >= new_blanks:
                        blank = " "
                    if wrd != "":
                        new_row += wrd + blank
                    z += 1
                r_text.append(new_row.strip())
            else:
                new_row = ""
                if phrase.count(" ") == 0:
                    r_text.append(phrase)
                    continue
                count = new_blanks // phrase.count(" ") #!!!! division by zero sea-sick.grow #201
                rep_str = " " + " "*count
                temp_row = phrase.replace(" ", rep_str)
                t_count = new_blanks % phrase.count(" ")
                t_rep_str = rep_str + " "
                temp_row = temp_row.split(rep_str,t_count)
                for word in temp_row:
                    new_row += word + t_rep_str
                r_text.append(new_row)
        elif phrase == txt[-1] or len(phrase) == length:
            r_text.append(phrase)

    return r_text



def main():
    print("Enter text rows. Quit by entering an empty row.")
    text = read_input()
    length = int(input("Enter the number of characters per line: "))
    text = break_text(text,length)
    for row in text:
        print(row)

main()


"""
CHAPTER VIII - CONCERNING THOSE WHO HAVE OBTAINED A PRINCIPALITY BY
WICKEDNESS
Although a prince may rise from a private station in two ways, neither
of which can be entirely attributed to fortune or genius, yet it is
manifest to me that I must not be silent on them, although one could be
more copiously treated when I discuss republics. These methods are
when, either by some wicked or nefarious ways, one ascends to the
principality, or when by the favour of his fellow-citizens a private
person becomes the prince of his country. And speaking of the first
method, it will be illustrated by two examples--one ancient, the other
modern--and without entering further into the subject, I consider these
two examples will suffice those who may be compelled to follow them.


Call me Ishmael. Some years ago.never mind how long precisely.having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen and
regulating the circulation. Whenever I find myself growing grim about
the mouth; whenever it is a damp, drizzly November in my soul; whenever
I find myself involuntarily pausing before coffin warehouses, and
bringing up the rear of every funeral I meet; and especially whenever
my hypos get such an upper hand of me, that it requires a strong moral
principle to prevent me from deliberately stepping into the street, and
methodically knocking people.s hats off.then, I account it high time to
get to sea as soon as I can. This is my substitute for pistol and ball.
With a philosophical flourish Cato throws himself upon his sword; I
quietly take to the ship. There is nothing surprising in this. If they
but knew it, almost all men in their degree, some time or other,
cherish very nearly the same feelings towards the ocean with me.
There now is your insular city of the Manhattoes, belted round by
wharves as Indian isles by coral reefs.commerce surrounds it with her
surf. Right and left, the streets take you waterward. Its extreme
downtown is the battery, where that noble mole is washed by waves, and
cooled by breezes, which a few hours previous were out of sight of
land. Look at the crowds of water-gazers there.
Circumambulate the city of a dreamy Sabbath afternoon. Go from Corlears
Hook to Coenties Slip, and from thence, by Whitehall, northward. What
do you see?.Posted like silent sentinels all around the town, stand
thousands upon thousands of mortal men fixed in ocean reveries. Some
leaning against the spiles; some seated upon the pier-heads; some
looking over the bulwarks of ships from China; some high aloft in the
rigging, as if striving to get a still better seaward peep. But these
are all landsmen; of week days pent up in lath and plaster.tied to
counters, nailed to benches, clinched to desks. How then is this? Are
the green fields gone? What do they here?
But look! here come more crowds, pacing straight for the water, and
seemingly bound for a dive. Strange! Nothing will content them but the
extremest limit of the land; loitering under the shady lee of yonder
warehouses will not suffice. No. They must get just as nigh the water
as they possibly can without falling in. And there they stand.miles of
them.leagues. Inlanders all, they come from lanes and alleys, streets
and avenues.north, east, south, and west. Yet here they all unite. Tell
me, does the magnetic virtue of the needles of the compasses of all
those ships attract them thither?
Once more. Say you are in the country; in some high land of lakes. Take
almost any path you please, and ten to one it carries you down in a
dale, and leaves you there by a pool in the stream. There is magic in
it. Let the most absent-minded of men be plunged in his deepest
reveries.stand that man on his legs, set his feet a-going, and he will
infallibly lead you to water, if water there be in all that region.
Should you ever be athirst in the great American desert, try this
experiment, if your caravan happen to be supplied with a metaphysical
professor. Yes, as every one knows, meditation and water are wedded for
ever.
But here is an artist. He desires to paint you the dreamiest, shadiest,
quietest, most enchanting bit of romantic landscape in all the valley
of the Saco. What is the chief element he employs? There stand his
trees, each with a hollow trunk, as if a hermit and a crucifix were
within; and here sleeps his meadow, and there sleep his cattle; and up
from yonder cottage goes a sleepy smoke. Deep into distant woodlands
winds a mazy way, reaching to overlapping spurs of mountains bathed in
their hill-side blue. But though the picture lies thus tranced, and
though this pine-tree shakes down its sighs like leaves upon this
shepherd.s head, yet all were vain, unless the shepherd.s eye were
fixed upon the magic stream before him. Go visit the Prairies in June,
when for scores on scores of miles you wade knee-deep among
Tiger-lilies.what is the one charm wanting?.Water.there is not a drop
of water there! Were Niagara but a cataract of sand, would you travel
your thousand miles to see it? Why did the poor poet of Tennessee, upon
suddenly receiving two handfuls of silver, deliberate whether to buy
him a coat, which he sadly needed, or invest his money in a pedestrian
trip to Rockaway Beach? Why is almost every robust healthy boy with a
robust healthy soul in him, at some time or other crazy to go to sea?
Why upon your first voyage as a passenger, did you yourself feel such a
mystical vibration, when first told that you and your ship were now out
of sight of land? Why did the old Persians hold the sea holy? Why did
the Greeks give it a separate deity, and own brother of Jove? Surely
all this is not without meaning. And still deeper the meaning of that
story of Narcissus, who because he could not grasp the tormenting, mild
image he saw in the fountain, plunged into it and was drowned. But that
same image, we ourselves see in all rivers and oceans. It is the image
of the ungraspable phantom of life; and this is the key to it all.
Now, when I say that I am in the habit of going to sea whenever I begin
to grow hazy about the eyes, and begin to be over conscious of my
lungs, I do not mean to have it inferred that I ever go to sea as a
passenger. For to go as a passenger you must needs have a purse, and a
purse is but a rag unless you have something in it. Besides, passengers
get sea-sick.grow quarrelsome.don.t sleep of nights.do not enjoy
themselves much, as a general thing;.no, I never go as a passenger;
nor, though I am something of a salt, do I ever go to sea as a
Commodore, or a Captain, or a Cook. I abandon the glory and distinction
of such offices to those who like them. For my part, I abominate all
honorable respectable toils, trials, and tribulations of every kind
whatsoever. It is quite as much as I can do to take care of myself,
without taking care of ships, barques, brigs, schooners, and what not.
And as for going as cook,.though I confess there is considerable glory
in that, a cook being a sort of officer on ship-board.yet, somehow, I
never fancied broiling fowls;.though once broiled, judiciously
buttered, and judgmatically salted and peppered, there is no one who
will speak more respectfully, not to say reverentially, of a broiled
fowl than I will. It is out of the idolatrous dotings of the old
Egyptians upon broiled ibis and roasted river horse, that you see the
mummies of those creatures in their huge bake-houses the pyramids.
No, when I go to sea, I go as a simple sailor, right before the mast,
plumb down into the forecastle, aloft there to the royal mast-head.
True, they rather order me about some, and make me jump from spar to
spar, like a grasshopper in a May meadow. And at first, this sort of
thing is unpleasant enough. It touches one.s sense of honor,
particularly if you come of an old established family in the land, the
Van Rensselaers, or Randolphs, or Hardicanutes. And more than all, if
just previous to putting your hand into the tar-pot, you have been
lording it as a country schoolmaster, making the tallest boys stand in
awe of you. The transition is a keen one, I assure you, from a
schoolmaster to a sailor, and requires a strong decoction of Seneca and
the Stoics to enable you to grin and bear it. But even this wears off
in time.
What of it, if some old hunks of a sea-captain orders me to get a broom
and sweep down the decks? What does that indignity amount to, weighed,
I mean, in the scales of the New Testament? Do you think the archangel
Gabriel thinks anything the less of me, because I promptly and
respectfully obey that old hunks in that particular instance? Who ain.t
a slave? Tell me that. Well, then, however the old sea-captains may
order me about.however they may thump and punch me about, I have the
satisfaction of knowing that it is all right; that everybody else is
one way or other served in much the same way.either in a physical or
metaphysical point of view, that is; and so the universal thump is
passed round, and all hands should rub each other.s shoulder-blades,
and be content.
Again, I always go to sea as a sailor, because they make a point of
paying me for my trouble, whereas they never pay passengers a single
penny that I ever heard of. On the contrary, passengers themselves must
pay. And there is all the difference in the world between paying and
being paid. The act of paying is perhaps the most uncomfortable
infliction that the two orchard thieves entailed upon us. But _being
paid_,.what will compare with it? The urbane activity with which a man
receives money is really marvellous, considering that we so earnestly
believe money to be the root of all earthly ills, and that on no
account can a monied man enter heaven. Ah! how cheerfully we consign
ourselves to perdition!
Finally, I always go to sea as a sailor, because of the wholesome
exercise and pure air of the fore-castle deck. For as in this world,
head winds are far more prevalent than winds from astern (that is, if
you never violate the Pythagorean maxim), so for the most part the
Commodore on the quarter-deck gets his atmosphere at second hand from
the sailors on the forecastle. He thinks he breathes it first; but not
so. In much the same way do the commonalty lead their leaders in many
other things, at the same time that the leaders little suspect it. But
wherefore it was that after having repeatedly smelt the sea as a
merchant sailor, I should now take it into my head to go on a whaling
voyage; this the invisible police officer of the Fates, who has the
constant surveillance of me, and secretly dogs me, and influences me in
some unaccountable way.he can better answer than any one else. And,
doubtless, my going on this whaling voyage, formed part of the grand
programme of Providence that was drawn up a long time ago. It came in
as a sort of brief interlude and solo between more extensive
performances.

"""