# ck-spider

- [Description](#description)
- [Parameters](#parameters)
- [Examples](#examples)
  - [Search by edition](#searching-by-edition)
  - [Search by cardname](#search-by-cardname)
- [Edition names list](#edition-name-list)
- [Known issues](#known-issues)

## Description
A simple cardkingdom spider.

## Parameters
+ `search_by`: currently works with only 2 values: **edition** and **cardname**.
+ `name`: the name which you are looking for.

> You can pass incomplete `name` values if you are searching by **cardname**.

## Examples 
### Searching by edition
```scrapy runspider mtgcards.py -a search_by=edition -a name=alpha -o edition.json```

### Search by cardname
```scrapy runspider mtgcards.py -a search_by=cardname -a name=black -o cardname.json```

## Edition name list

| Edition | Name |
|---------|------|
|3rd Edition|3rd edition|
|4th Edition|4th edition|
|5th Edition|5th edition|
|6th Edition|6th edition|
|7th Edition|7th edition|
|8th Edition|8th edition|
|9th Edition|9th edition|
|10th Edition|10th edition|
|2010 Core Set|2010 core set|
|2011 Core Set|2011 core set|
|2012 Core Set|2012 core set|
|2013 Core Set|2013 core set|
|2014 Core Set|2014 core set|
|2015 Core Set|2015 core set|
|Aether Revolt|aether revolt|
|Alara Reborn|alara reborn|
|Alliances|alliances|
|Alpha|alpha|
|Amonkhet|amonkhet|
|Anthologies|anthologies|
|Antiquities|antiquities|
|Apocalypse|apocalypse|
|Arabian Nights|arabian nights|
|Archenemy|archenemy|
|Archenemy - Nicol Bolas|archenemy nicol bolas|
|Art Series|art series|
|Avacyn Restored|avacyn restored|
|Battle for Zendikar|battle for zendikar|
|Battle Royale|battle royale|
|Battlebond|battlebond|
|Beatdown|beatdown|
|Beta|beta|
|Betrayers of Kamigawa|betrayers of kamigawa|
|Born of the Gods|born of the gods|
|Card Kingdom Tokens|card kingdom tokens|
|Challenger Decks 2018|challenger decks 2018|
|Challenger Decks 2019|challenger decks 2019|
|Challenger Decks 2020|challenger decks 2020|
|Champions of Kamigawa|champions of kamigawa|
|Chronicles|chronicles|
|Coldsnap|coldsnap|
|Coldsnap Theme Decks|coldsnap theme decks|
|Collectors Ed|collectors ed|
|Collectors Ed Intl|collectors ed intl|
|Commander|commander|
|Commander 2013|commander 2013|
|Commander 2014|commander 2014|
|Commander 2015|commander 2015|
|Commander 2016|commander 2016|
|Commander 2017|commander 2017|
|Commander 2018|commander 2018|
|Commander 2019|commander 2019|
|Commander Anthology|commander anthology|
|Commander Anthology Vol. II|commander anthology vol ii|
|Commander's Arsenal|commanders arsenal|
|Conflux|conflux|
|Conspiracy|conspiracy|
|Conspiracy - Take the Crown|conspiracy take the crown|
|Core Set 2019|core set 2019|
|Core Set 2020|core set 2020|
|Dark Ascension|dark ascension|
|Darksteel|darksteel|
|Deckmaster|deckmaster|
|Dissension|dissension|
|Dominaria|dominaria|
|Dragon's Maze|dragons maze|
|Dragons of Tarkir|dragons of tarkir|
|Duel Decks: Ajani Vs. Nicol Bolas|duel decks ajani vs nicol bolas|
|Duel Decks: Anthology|duel decks anthology|
|Duel Decks: Blessed Vs. Cursed|duel decks blessed vs cursed|
|Duel Decks: Divine Vs. Demonic|duel decks divine vs demonic|
|Duel Decks: Elspeth Vs. Kiora|duel decks elspeth vs kiora|
|Duel Decks: Elspeth Vs. Tezzeret|duel decks elspeth vs tezzeret|
|Duel Decks: Elves Vs. Goblins|duel decks elves vs goblins|
|Duel Decks: Elves Vs. Inventors|duel decks elves vs inventors|
|Duel Decks: Garruk Vs. Liliana|duel decks garruk vs liliana|
|Duel Decks: Heroes Vs. Monsters|duel decks heroes vs monsters|
|Duel Decks: Izzet Vs. Golgari|duel decks izzet vs golgari|
|Duel Decks: Jace Vs. Chandra|duel decks jace vs chandra|
|Duel Decks: Jace Vs. Vraska|duel decks jace vs vraska|
|Duel Decks: Knights Vs. Dragons|duel decks knights vs dragons|
|Duel Decks: Merfolk Vs. Goblins|duel decks merfolk vs goblins|
|Duel Decks: Mind Vs. Might|duel decks mind vs might|
|Duel Decks: Nissa Vs. Ob Nixilis|duel decks nissa vs ob nixilis|
|Duel Decks: Phyrexia Vs. The Coalition|duel decks phyrexia vs the coalition|
|Duel Decks: Sorin Vs. Tibalt|duel decks sorin vs tibalt|
|Duel Decks: Speed Vs. Cunning|duel decks speed vs cunning|
|Duel Decks: Venser Vs. Koth|duel decks venser vs koth|
|Duel Decks: Zendikar Vs. Eldrazi|duel decks zendikar vs eldrazi|
|Duels of the Planeswalkers|duels of the planeswalkers|
|Eldritch Moon|eldritch moon|
|Eternal Masters|eternal masters|
|Eventide|eventide|
|Exodus|exodus|
|Explorers of Ixalan|explorers of ixalan|
|Fallen Empires|fallen empires|
|Fate Reforged|fate reforged|
|Fifth Dawn|fifth dawn|
|From the Vault: Angels|from the vault angels|
|From the Vault: Annihilation|from the vault annihilation|
|From the Vault: Dragons|from the vault dragons|
|From the Vault: Exiled|from the vault exiled|
|From the Vault: Legends|from the vault legends|
|From the Vault: Lore|from the vault lore|
|From the Vault: Realms|from the vault realms|
|From the Vault: Relics|from the vault relics|
|From the Vault: Transform|from the vault transform|
|From the Vault: Twenty|from the vault twenty|
|Future Sight|future sight|
|Game Night|game night|
|Game Night 2019|game night 2019|
|Gatecrash|gatecrash|
|Gift Pack 2017|gift pack 2017|
|Global Series: Jiang Yanggu &amp; Mu Yanling|global series jiang yanggu mu yanling|
|Guildpact|guildpact|
|Guilds of Ravnica|guilds of ravnica|
|Guilds of Ravnica: Guild Kits|guilds of ravnica guild kits|
|Homelands|homelands|
|Hour of Devastation|hour of devastation|
|Ice Age|ice age|
|Iconic Masters|iconic masters|
|Innistrad|innistrad|
|Invasion|invasion|
|Ixalan|ixalan|
|Journey into Nyx|journey into nyx|
|Judgment|judgment|
|Kaladesh|kaladesh|
|Khans of Tarkir|khans of tarkir|
|Legends|legends|
|Legions|legions|
|Lorwyn|lorwyn|
|Magic Origins|magic origins|
|Masterpiece Series: Expeditions|masterpiece series expeditions|
|Masterpiece Series: Inventions|masterpiece series inventions|
|Masterpiece Series: Invocations|masterpiece series invocations|
|Masterpiece Series: Mythic Edition|masterpiece series mythic edition|
|Masters 25|masters 25|
|Mercadian Masques|mercadian masques|
|Mirage|mirage|
|Mirrodin|mirrodin|
|Mirrodin Besieged|mirrodin besieged|
|Modern Event Deck|modern event deck|
|Modern Horizons|modern horizons|
|Modern Masters|modern masters|
|Modern Masters 2015|modern masters 2015|
|Modern Masters 2017|modern masters 2017|
|Morningtide|morningtide|
|Mystery Booster|mystery booster|
|Nemesis|nemesis|
|New Phyrexia|new phyrexia|
|Oath of the Gatewatch|oath of the gatewatch|
|Odyssey|odyssey|
|Onslaught|onslaught|
|Planar Chaos|planar chaos|
|Planechase|planechase|
|Planechase 2012|planechase 2012|
|Planechase Anthology|planechase anthology|
|Planeshift|planeshift|
|Portal|portal|
|Portal 3K|portal 3k|
|Portal II|portal ii|
|Premium Deck Series: Fire &amp; Lightning|premium deck series fire lightning|
|Premium Deck Series: Graveborn|premium deck series graveborn|
|Premium Deck Series: Slivers|premium deck series slivers|
|Promo Pack|promo pack|
|Promotional|promotional|
|Prophecy|prophecy|
|Ravnica|ravnica|
|Ravnica Allegiance|ravnica allegiance|
|Ravnica Allegiance: Guild Kits|ravnica allegiance guild kits|
|Return to Ravnica|return to ravnica|
|Rise of the Eldrazi|rise of the eldrazi|
|Rivals of Ixalan|rivals of ixalan|
|Saviors of Kamigawa|saviors of kamigawa|
|Scars of Mirrodin|scars of mirrodin|
|Scourge|scourge|
|Secret Lair|secret lair|
|Shadowmoor|shadowmoor|
|Shadows Over Innistrad|shadows over innistrad|
|Shards of Alara|shards of alara|
|Signature Spellbook: Gideon|signature spellbook gideon|
|Signature Spellbook: Jace|signature spellbook jace|
|Starter 1999|starter 1999|
|Starter 2000|starter 2000|
|Stronghold|stronghold|
|Tempest|tempest|
|The Dark|the dark|
|Theros|theros|
|Theros Beyond Death|theros beyond death|
|Theros Beyond Death Variants|theros beyond death variants|
|Throne of Eldraine|throne of eldraine|
|Throne of Eldraine Variants|throne of eldraine variants|
|Time Spiral|time spiral|
|Timeshifted|timeshifted|
|Torment|torment|
|Ultimate Box Topper|ultimate box topper|
|Ultimate Masters|ultimate masters|
|Unglued|unglued|
|Unhinged|unhinged|
|Unlimited|unlimited|
|Unsanctioned|unsanctioned|
|Unstable|unstable|
|Urza's Destiny|urzas destiny|
|Urza's Legacy|urzas legacy|
|Urza's Saga|urzas saga|
|Vanguard|vanguard|
|Visions|visions|
|War of the Spark|war of the spark|
|War of the Spark JPN Planeswalkers|war of the spark jpn planeswalkers|
|Weatherlight|weatherlight|
|World Championships|world championships|
|Worldwake|worldwake|
|Zendikar|zendikar|

> Updated until Theros Beyond Death.

## Known issues
+ Can't parse correctly flavor texts if they contain html tags.
+ Can't parse correctly mana costs because they are `<img>` tags and there isn't currently an string representation of them.

[#top](#ck-spider)
