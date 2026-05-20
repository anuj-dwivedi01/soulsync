# seed.py
import json
from app import create_app, db
from app.models import Mode, Question

app = create_app()

def seed_database():
    with app.app_context():
        print("⚡ Resetting database schema...")
        db.drop_all()
        db.create_all()

        print("🌱 Seeding relationship modes...")
        modes = [
            Mode(name="Lovers", description="Deep emotional intimacy, attachment loops, and romantic mapping.", theme_color="rose"),
            Mode(name="Best Friends", description="Unfiltered trust, platonic safety, and life-alignment dynamics.", theme_color="emerald"),
            Mode(name="Gaming Friends", description="Synergy matrices, strategic compatibility, and communication under pressure.", theme_color="cyan"),
            Mode(name="Work Partners", description="Professional friction limits, output execution alignment, and leadership style synchronization.", theme_color="amber"),
            Mode(name="Crush / Unspoken", description="Vulnerability readings, subconscious micro-signals, and tension mapping.", theme_color="purple"),
            Mode(name="Siblings / Family", description="Long-term behavioral conditioning, core childhood trust, and loyalty frameworks.", theme_color="blue"),
            Mode(name="New Dates", description="First-impression matrices, boundary testing, and red flag tracking.", theme_color="teal"),
            Mode(name="Long-Distance", description="Digital trust matrices, object permanence, and reunion pacing.", theme_color="orange"),
            Mode(name="The Closure / Exes", description="Autopsy of failed dynamics, lingering resentments, and psychological closure.", theme_color="slate")
        ]
        
        for mode in modes:
            db.session.add(mode)
        db.session.commit()

        # Fetch the Lovers mode ID dynamically to bind questions properly
        lovers_mode = Mode.query.filter_by(name="Lovers").first()
        best_friends_mode = Mode.query.filter_by(name="Best Friends").first()
        gaming_friends_mode = Mode.query.filter_by(name="Gaming Friends").first()
        work_partners_mode = Mode.query.filter_by(name="Work Partners").first()
        crush_mode = Mode.query.filter_by(name="Crush / Unspoken").first()
        siblings_mode = Mode.query.filter_by(name="Siblings / Family").first()
        new_dates_mode = Mode.query.filter_by(name="New Dates").first()
        long_distance_mode = Mode.query.filter_by(name="Long-Distance").first()
        closure_mode =Mode.query.filter_by(name="The Closure / Exes").first()

        print("🧠 Compiling comprehensive psychological question matrix for Lovers Mode...")
        
        questions_data = [
            # ==========================================
            # LOVERS MODE - SET 1: CORE CORE BASELINE
            # ==========================================
            {
                "text": "When something emotionally difficult happens, what do you naturally want first?",
                "options": ["Emotional comfort", "Practical solutions", "Space before talking", "Quiet presence"],
                "dimension": "Emotional Needs", "question_type": "alignment"
            },
            {
                "text": "When I am upset, what do I usually expect from you without directly asking for it?",
                "options": ["Immediate reassurance", "Patience and understanding", "Problem-solving", "Time and emotional space"],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },
            {
                "text": "Which of these hurts you more in a relationship?",
                "options": ["Feeling ignored", "Feeling misunderstood", "Feeling controlled", "Feeling emotionally distant"],
                "dimension": "Emotional Needs", "question_type": "alignment"
            },
            {
                "text": "What makes me feel emotionally safest with someone?",
                "options": ["Consistency", "Honesty", "Emotional openness", "Loyalty during hard times"],
                "dimension": "Trust", "question_type": "prediction"
            },
            {
                "text": "During misunderstandings, what matters more to you?",
                "options": ["Tone of conversation", "Intent behind words", "Quick resolution", "Feeling emotionally heard"],
                "dimension": "Communication", "question_type": "alignment"
            },
            {
                "text": "If I suddenly become quieter than usual, what is your first instinct?",
                "options": ["Ask directly what happened", "Give me space first", "Assume something is wrong", "Wait for me to open up naturally"],
                "dimension": "Communication", "question_type": "prediction"
            },

            # ==========================================
            # LOVERS MODE - SET 2: VULNERABILITY & ATTACHMENT
            # ==========================================
            {
                "text": "When sharing a deeply insecure thought with your partner, what is your hidden fear?",
                "options": ["Being judged or criticized", "Having my feelings minimized", "It being used against me later", "Them looking at me differently"],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "What is my absolute biggest subconscious trigger during a heated argument?",
                "options": ["Being interrupted or spoken over", "The fear that you are walking away", "Feeling like my point is ignored", "A cold or indifferent tone of voice"],
                "dimension": "Conflict Handling", "question_type": "prediction"
            },
            {
                "text": "If you notice your partner is gradually pulling back emotionally, how do you respond?",
                "options": ["Anxiously push for immediate answers", "Give them space while overthinking", "Match their distance to protect myself", "Calmly state what I see and wait"],
                "dimension": "Communication", "question_type": "alignment"
            },
            {
                "text": "How do I naturally prefer to recharge after a high-stress emotional week?",
                "options": ["Intense one-on-one quality time", "Absolute quiet isolation alone", "Doing physical activities together", "Ventilation through deep processing calls"],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },

            # ==========================================
            # LOVERS MODE - SET 3: FRICTION & BOUNDARIES
            # ==========================================
            {
                "text": "Which behavior makes you close down and stop communicating entirely?",
                "options": ["Sarcasm and passive aggression", "Defensive deflecting of blame", "Emotional stonewalling/silence", "Raising voices and loud tones"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },
            {
                "text": "How do I feel about external boundaries with friends or family regarding our relationship?",
                "options": ["Keep our business 100% private", "Okay to share minor things for advice", "Rely on external systems heavily", "Open validation matters to me"],
                "dimension": "Trust", "question_type": "prediction"
            },
            {
                "text": "When an apology is given, what makes it feel genuine to you?",
                "options": ["An explicit validation of my hurt", "An immediate change in behavior", "A logical explanation of what happened", "Physical reassurance and comfort"],
                "dimension": "Communication", "question_type": "alignment"
            },
            {
                "text": "What type of emotional validation do I need most when I make a major mistake?",
                "options": ["Reassurance that you still love me", "Logical assistance to fix it", "Space to process my guilt alone", "No judgment, just drop the topic"],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },
            {
                "text": "When we are arguing, what is the fastest way for you to completely lose my trust?",
                "options": ["Screaming or losing emotional control", "Walking away mid-sentence", "Bringing up my past mistakes", "Using my deepest insecurities against me"],
                "dimension": "Trust", "question_type": "prediction"
            },

            # ==========================================
            # LOVERS MODE - SET 4: GROWTH & LONG-TERM VISION
            # ==========================================
            {
                "text": "What does 'growing together' mean most explicitly to you?",
                "options": ["Aligning our career and financial tracks", "Evolving our emotional maturity levels", "Supporting separate personal dreams", "Building a shared physical lifestyle"],
                "dimension": "Emotional Needs", "question_type": "alignment"
            },
            {
                "text": "If our relationship fell into a boring, repetitive routine, how would I react?",
                "options": ["Directly address it and suggest changes", "Slowly become restless and anxious", "Accept it as a peaceful, stable phase", "Subconsciously look for outside distractions"],
                "dimension": "Communication", "question_type": "prediction"
            },
            {
                "text": "What is the ultimate foundation that keeps you committed during rough moments?",
                "options": ["Our history and everything we built", "The depth of our emotional friendship", "Our shared values and life vision", "An unshakeable gut feelings of loyalty"],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "When making massive life choices, what do I prioritize most?",
                "options": ["Long-term security and stability", "Immediate emotional fulfillment/happiness", "Personal growth and freedom", "Whatever makes our partnership easier"],
                "dimension": "Conflict Handling", "question_type": "prediction"
            },
            {
                "text": "What is my biggest underlying fear about our future together?",
                "options": ["That we will lose our romantic spark", "That we will become overwhelmed by stress", "That one of us will outgrow the other", "That we will fall into a boring, roommate routine"],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },

            # ==========================================
            # LOVERS MODE - SET 5: THE UNCONSCIOUS ROOT
            # ==========================================
            {
                "text": "Which form of connection makes you feel the most intimately valued?",
                "options": ["Unprompted, deep verbal praise", "Quiet, prolonged physical touch", "Unexpected acts of helpful service", "Undivided attention without a phone"],
                "dimension": "Emotional Needs", "question_type": "alignment"
            },
            {
                "text": "If I am forced to choose between being completely right or keeping the peace, what do I do?",
                "options": ["Fight aggressively to prove my logic", "Give in completely to end the tension", "Passively keep bringing it up later", "State my side clearly then drop it"],
                "dimension": "Conflict Handling", "question_type": "prediction"
            },
            {
                "text": "What underlying element makes you lose respect for a partner the fastest?",
                "options": ["A pattern of broken minor promises", "Emotional cowardice or hiding truth", "Lack of ambition or personal growth", "Cruelty or disrespect during fights"],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "If you feel completely disconnected from your partner, what is the first thing you unconsciously do?",
                "options": ["Start picking small fights to get attention", "Withdraw and focus entirely on work or hobbies", "Seek validation from external friends", "Try to force extreme intimacy very quickly"],
                "dimension": "Communication", "question_type": "alignment"
            },
            {
                "text": "What is my default internal coping mechanism when I feel deeply overwhelmed?",
                "options": ["Isolating into complete mental silence", "Over-analyzing and talking excessively", "Seeking instant physical distraction", "Becoming easily irritable over tiny things"],
                "dimension": "Communication", "question_type": "prediction"
            }
        ]
        print("🤝 Compiling 25-question psychological matrix for Best Friends Mode...")
        
        best_friends_data = [
            # ==========================================
            # SECTION 1: CORE PLATONIC TRUST
            # ==========================================
            {
                "text": "What is the absolute fastest way for a friend to lose your trust?",
                "options": ["Lying to my face", "Sharing a secret I told them", "Defending someone who hurt me", "Slowly ghosting without explanation"],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "If I am clearly making a terrible life decision, what do you expect me to do?",
                "options": ["Tell you brutally and honestly", "Give gentle advice but let you decide", "Support you even if it's a mistake", "Intervene and try to stop you"],
                "dimension": "Conflict Handling", "question_type": "prediction"
            },
            {
                "text": "When you are going through a rough patch, what kind of friend do you need most?",
                "options": ["The one who distracts me with fun", "The one who sits and listens to me vent", "The one who helps me fix the problem", "The one who gives me space but checks in"],
                "dimension": "Emotional Needs", "question_type": "alignment"
            },
            {
                "text": "What makes me feel the most valued in our friendship?",
                "options": ["When you remember small details about my life", "When you show up during emergencies", "When we can just sit in comfortable silence", "When you hype me up in front of others"],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },
            {
                "text": "How do you view long periods of no communication with a close friend?",
                "options": ["It makes me feel distant and disconnected", "It's completely normal, we pick up where we left off", "I assume they are mad at me", "It depends on if they left me on read"],
                "dimension": "Communication", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 2: COMMUNICATION & HONESTY
            # ==========================================
            {
                "text": "If you are secretly annoyed by something I did, how do you usually handle it?",
                "options": ["Drop passive-aggressive hints", "Bring it up directly but casually", "Hold it in until I explode later", "Distance myself until I get over it"],
                "dimension": "Communication", "question_type": "alignment"
            },
            {
                "text": "When I text you 'We need to talk', what is my most likely internal state?",
                "options": ["I am furious and ready to argue", "I am extremely anxious and need comfort", "I have exciting drama to share", "I am being completely serious and analytical"],
                "dimension": "Communication", "question_type": "prediction"
            },
            {
                "text": "What is your philosophy on 'brutal honesty' in friendship?",
                "options": ["It's required; never sugarcoat things", "It should only be used if I ask for it", "Delivery matters more than the truth itself", "I prefer supportive white lies over harsh truths"],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "If someone starts talking badly about me to you, how do I expect you to react?",
                "options": ["Immediately shut them down aggressively", "Calmly defend me with logic", "Listen but report back to me later", "Walk away from the conversation"],
                "dimension": "Conflict Handling", "question_type": "prediction"
            },
            {
                "text": "What kind of humor strengthens a friendship the most for you?",
                "options": ["Dark, sarcastic, and slightly mean banter", "Silly, goofy, and lighthearted inside jokes", "Deeply contextual, observational humor", "Sending each other unhinged internet memes"],
                "dimension": "Communication", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 3: BOUNDARIES & CONFLICT
            # ==========================================
            {
                "text": "If we get into a massive argument, what is your first instinct?",
                "options": ["Apologize quickly just to end the tension", "Dig my heels in and prove I am right", "Stop talking to you for a few days to cool off", "Try to make a joke to break the ice"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },
            {
                "text": "Which of my boundaries is the most dangerous to cross?",
                "options": ["Disrespecting my family or partner", "Wasting my time or money", "Making me feel stupid in public", "Ignoring my clear 'no'"],
                "dimension": "Trust", "question_type": "prediction"
            },
            {
                "text": "How do you feel about your best friend becoming very close with someone you dislike?",
                "options": ["It feels like a massive betrayal", "I don't care, their relationships are separate", "It makes me highly uncomfortable but I won't say it", "I will judge them for it, but tolerate it"],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "When I am completely overwhelmed with stress, what is the WORST thing you could say?",
                "options": ["'It's not that big of a deal.'", "'You brought this on yourself.'", "'Just calm down.'", "Saying nothing and ignoring it."],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },
            {
                "text": "What is your approach to borrowing money between best friends?",
                "options": ["Never do it, it ruins friendships", "Only small amounts that I treat as gifts", "I keep a strict mental ledger of who owes who", "What's mine is yours, no tracking needed"],
                "dimension": "Trust", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 4: SUPPORT & LOYALTY
            # ==========================================
            {
                "text": "What does true loyalty look like to you?",
                "options": ["Defending me when I am not in the room", "Dropping everything when I need you", "Never judging me for my darkest secrets", "Always telling me the truth, even if it hurts"],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "If I achieve something massive, how do I prefer to be celebrated?",
                "options": ["A loud, public acknowledgment", "A quiet, sincere one-on-one conversation", "Being treated to a nice dinner or drinks", "Just hearing 'I'm proud of you'"],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },
            {
                "text": "If you strongly dislike my new romantic partner, what do you do?",
                "options": ["Tell you immediately before you get attached", "Keep it to myself unless they hurt you", "Actively try to sabotage it", "Slowly distance myself from the dynamic"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },
            {
                "text": "What is the primary reason I would ever cut a friend off permanently?",
                "options": ["A massive, sudden betrayal", "A slow realization that the effort is one-sided", "They crossed a core moral boundary of mine", "Consistent, subtle disrespect over time"],
                "dimension": "Conflict Handling", "question_type": "prediction"
            },
            {
                "text": "How do you handle a friend who is constantly making themselves the victim?",
                "options": ["I slowly stop replying to their complaints", "I validate them because that's what friends do", "I harshly call them out on their behavior", "I try to actively fix their problems for them"],
                "dimension": "Emotional Needs", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 5: GROWTH & TIME
            # ==========================================
            {
                "text": "As we get older, what do you think is the biggest threat to our friendship?",
                "options": ["Moving to different cities", "Getting consumed by romantic relationships/marriage", "Growing into different value systems", "Just getting too busy with careers"],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "What is my absolute favorite way to spend a Saturday with a best friend?",
                "options": ["Going out and socializing at an event", "Doing absolutely nothing on a couch together", "Going on a spontaneous adventure/trip", "Working on our own separate hobbies in the same room"],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },
            {
                "text": "How do you view 'maintenance' in a friendship?",
                "options": ["It requires daily check-ins", "Weekly catch-ups are enough", "True friendship requires zero maintenance", "It's purely about effort during big moments"],
                "dimension": "Communication", "question_type": "alignment"
            },
            {
                "text": "What is the one trait you possess that I value the most?",
                "options": ["Your unshakeable reliability", "Your sense of humor and ability to make me laugh", "Your deep emotional intelligence", "Your blunt, unfiltered honesty"],
                "dimension": "Communication", "question_type": "prediction"
            },
            {
                "text": "At the end of our lives, what makes a friendship 'successful' to you?",
                "options": ["The sheer length of time we stayed together", "The number of crazy memories we made", "The fact that we helped each other grow", "The absolute safety and lack of judgment we shared"],
                "dimension": "Emotional Needs", "question_type": "alignment"
            }
        ]
        print("🎮 Compiling 25-question psychological matrix for Gaming Friends Mode...")
        
        gaming_friends_data = [
            # ==========================================
            # SECTION 1: THE LOADOUT (Playstyle Synergy)
            # ==========================================
            {
                "text": "We just lost 3 ranked matches in a row. What is your natural instinct?",
                "options": ["Rage quit and play something else", "Insta-queue again to win it back", "Take a 10-minute break to reset", "Blame the game or random teammates"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },
            {
                "text": "What is my absolute favorite role or playstyle in a squad?",
                "options": ["The aggressive frontline fragger", "The strategic support/healer", "The quiet flanker/sniper", "The loud shotcaller/leader"],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },
            {
                "text": "What matters more to you when picking a game to play together?",
                "options": ["High-stakes competitive ranking", "Relaxing and turning our brains off", "A deep, immersive story co-op", "Just messing around and trolling"],
                "dimension": "Communication", "question_type": "alignment"
            },
            {
                "text": "If I am completely silent in the lobby between matches, what does it usually mean?",
                "options": ["I am tilted and angry", "I am just looking at my phone", "I am hyper-focused for the next game", "I am getting tired and want to log off"],
                "dimension": "Communication", "question_type": "prediction"
            },
            {
                "text": "When the team is panicking during a chaotic moment, who usually takes control?",
                "options": ["I do, I start yelling instructions", "You do, you naturally take the lead", "Nobody, we all scream at the same time", "We go completely quiet and focus"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 2: COMMS & SHOTCALLING
            # ==========================================
            {
                "text": "During an intense clutch moment, what kind of comms do you want?",
                "options": ["Absolute dead silence", "Only critical enemy locations/info", "Hype and encouragement", "Micromanaging and telling me what to do"],
                "dimension": "Communication", "question_type": "alignment"
            },
            {
                "text": "How do I react when someone 'backseat-games' me while I'm alive?",
                "options": ["I ignore them completely", "I get annoyed and tell them to shut up", "I actually listen and follow their advice", "I panic and mess up my play"],
                "dimension": "Conflict Handling", "question_type": "prediction"
            },
            {
                "text": "How do you prefer to give feedback if I make a stupid mistake?",
                "options": ["Roast you relentlessly for it", "Give constructive advice on what to do next time", "Stay quiet so I don't tilt you", "Blame the game mechanics instead"],
                "dimension": "Communication", "question_type": "alignment"
            },
            {
                "text": "What is my absolute worst communication habit during a fight?",
                "options": ["Giving terrible or wrong callouts", "Yelling too loud in the mic", "Going completely silent", "Complaining about lag before I'm even dead"],
                "dimension": "Communication", "question_type": "prediction"
            },
            {
                "text": "If you heavily disagree with the squad's strategy mid-game, what do you do?",
                "options": ["Follow the bad call anyway as a team", "Argue and try to change their minds", "Go do my own thing silently", "Complain but still do it"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 3: TILT & TOXICITY
            # ==========================================
            {
                "text": "What triggers your 'tilt' the fastest in a gaming session?",
                "options": ["My own stupid mistakes", "Toxic opponents trash-talking", "Bad internet/lag/game bugs", "Teammates not listening to comms"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },
            {
                "text": "When I am fully tilted and angry, how do I usually sound?",
                "options": ["Screaming and aggressive", "Deep sighs and passive-aggressive comments", "Dead, cold silence", "I start making self-deprecating jokes"],
                "dimension": "Communication", "question_type": "prediction"
            },
            {
                "text": "If our random teammate is being incredibly toxic on the mic, how do you handle it?",
                "options": ["Mute them instantly", "Argue back and troll them", "Try to calm them down and win", "Enable them and join in the toxicity"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },
            {
                "text": "If I completely throw the match by mistake, what do I want you to say?",
                "options": ["'It happens, don't worry about it.'", "Roast me so we can laugh it off", "Tell me exactly what I did wrong", "Say literally nothing"],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },
            {
                "text": "How quickly do you forgive a gaming friend who snaps at you over a game?",
                "options": ["Instantly, it's just a game", "After a quick apology", "I hold a grudge for the rest of the session", "I will bring it up again tomorrow"],
                "dimension": "Trust", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 4: LOYALTY & THE GRIND
            # ==========================================
            {
                "text": "If a higher-ranked group invites you while we are playing, what do you do?",
                "options": ["Leave instantly for the better lobby", "Ask if there is room for both of us", "Tell them no, I'm already playing with my duo", "Make up an excuse to leave politely"],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "What is the main reason I actually log on to play with you?",
                "options": ["To grind ranks and sweat", "To use the game as a background to talk about life", "Just to laugh and troll", "Because I hate playing solo"],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },
            {
                "text": "How do you feel about playing our 'main game' without your duo/squad?",
                "options": ["I play solo all the time", "I only play alternative modes solo", "It feels empty, I wait for you guys", "I will secretly play with another group"],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "If we find a rare, high-value loot drop, do I share it or keep it?",
                "options": ["Hoard it for myself immediately", "Offer it to whoever needs it most", "Make a trade for it", "Give it to you because you carry"],
                "dimension": "Trust", "question_type": "prediction"
            },
            {
                "text": "What builds ultimate trust for you in a gaming partner?",
                "options": ["They never leave me to die alone", "They drop me their best weapons/loot", "They always have my back in the voice chat", "They play consistently at the same times"],
                "dimension": "Trust", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 5: THE CORE VIBE
            # ==========================================
            {
                "text": "When the gaming session ends, how do you usually log off?",
                "options": ["'Alright I'm getting off, peace.' *Insta-leaves*", "We stay in the lobby talking for 20 more minutes", "An abrupt rage quit after a bad loss", "Making plans for exactly when we play tomorrow"],
                "dimension": "Communication", "question_type": "alignment"
            },
            {
                "text": "What makes a gaming session feel like a '10/10' for me?",
                "options": ["Gaining massive amounts of rank/elo", "Pulling off insane clutch plays", "Non-stop laughing until it hurts", "Finally beating a level we were stuck on"],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },
            {
                "text": "Do you care more about our rank/win-rate or the actual fun of the session?",
                "options": ["100% Rank. Winning is fun.", "Mostly fun, but I hate losing constantly.", "100% Fun. I don't care about my rank.", "I only care about my individual stats."],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "If I decide to quit playing a specific game forever, what is the most likely reason?",
                "options": ["The developers ruined it with updates", "I got too angry at the toxic community", "My friends stopped playing it", "I just got bored and found a new hyper-fixation"],
                "dimension": "Conflict Handling", "question_type": "prediction"
            },
            {
                "text": "What is the highest compliment a gaming partner can give you?",
                "options": ["'You carried us that game.'", "'Your callouts are actually insane.'", "'I only have fun playing this when you are on.'", "'You are the most reliable teammate.'"],
                "dimension": "Emotional Needs", "question_type": "alignment"
            }
        ]
        print("💼 Compiling 25-question psychological matrix for Work Partners Mode...")
        
        work_partners_data = [
            # ==========================================
            # SECTION 1: ACCOUNTABILITY & WORK ETHIC
            # ==========================================
            {
                "text": "If we miss a major project deadline, what is your immediate reaction?",
                "options": ["Analyze exactly where the process failed", "Take the blame to protect the team", "Start working overtime to fix it instantly", "Defend our work to leadership"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },
            {
                "text": "If a colleague unfairly throws me under the bus in a meeting, how do I react?",
                "options": ["Call them out professionally right there", "Stay quiet but document everything", "Confront them aggressively after the meeting", "Ignore it and let my work speak for itself"],
                "dimension": "Conflict Handling", "question_type": "prediction"
            },
            {
                "text": "How do you prefer to receive critical feedback on your work?",
                "options": ["Blunt, direct, and without sugarcoating", "Sandwiched between positive compliments", "In a private, scheduled 1-on-1 meeting", "Written down via email/message so I can process it"],
                "dimension": "Communication", "question_type": "alignment"
            },
            {
                "text": "What makes me feel the most valued in a professional setting?",
                "options": ["Public recognition and praise", "Financial bonuses and raises", "Being given complete autonomy and trust", "Having my ideas implemented by the team"],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },
            {
                "text": "What is your stance on micromanagement?",
                "options": ["I hate it; tell me the goal and leave me alone", "I actually like frequent check-ins for alignment", "It's necessary for new projects, but not routine work", "I will actively rebel against a micromanager"],
                "dimension": "Trust", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 2: COMMUNICATION & MEETINGS
            # ==========================================
            {
                "text": "What is your preferred method of daily team communication?",
                "options": ["Quick, informal Slack/Teams messages", "Detailed, structured emails", "Scheduled video calls", "Walking up to someone's desk (in-person)"],
                "dimension": "Communication", "question_type": "alignment"
            },
            {
                "text": "If I am completely silent during a brainstorming meeting, what does it mean?",
                "options": ["I am deeply analyzing what is being said", "I completely disagree but don't want to argue", "I am zoned out or working on something else", "I am waiting for the right moment to speak"],
                "dimension": "Communication", "question_type": "prediction"
            },
            {
                "text": "If we strongly disagree on the creative direction of a project, how do you resolve it?",
                "options": ["Rely on hard data and metrics", "Compromise and merge both ideas", "Defer to whoever has more seniority", "Debate until one of us concedes"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },
            {
                "text": "What is my absolute biggest pet peeve regarding workplace communication?",
                "options": ["Meetings that could have been an email", "People taking days to reply to messages", "Vague instructions with no clear objective", "Passive-aggressive corporate jargon"],
                "dimension": "Communication", "question_type": "prediction"
            },
            {
                "text": "How do you approach a massive, unorganized project?",
                "options": ["Build a massive spreadsheet/tracker first", "Start executing the easiest tasks immediately", "Call a meeting to delegate roles", "Panic slightly, then hyper-focus"],
                "dimension": "Trust", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 3: STRESS & CRISIS MANAGEMENT
            # ==========================================
            {
                "text": "When a project unexpectedly catches on fire, what is your first instinct?",
                "options": ["Take total control and start delegating", "Quietly put my head down and do the heavy lifting", "Escalate to management immediately", "Look for a quick band-aid solution"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },
            {
                "text": "How do I need to be supported during a massive 'crunch time' week?",
                "options": ["Take administrative tasks off my plate", "Bring me coffee/food and leave me alone", "Actively collaborate and brainstorm with me", "Constantly reassure me that we will finish"],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },
            {
                "text": "If you have to hand off a critical piece of your project to a partner, how do you feel?",
                "options": ["Completely fine, I trust them", "Anxious; I will secretly double-check their work", "Relieved to have it off my desk", "I'd rather just work late and do it myself"],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "How do I generally react to massive last-minute scope changes from a client/boss?",
                "options": ["Complain loudly, but get it done", "Push back professionally and say no", "Accept it quietly and internalize the stress", "Treat it as an exciting new challenge"],
                "dimension": "Conflict Handling", "question_type": "prediction"
            },
            {
                "text": "Where do you draw the line on work-life balance?",
                "options": ["I log off exactly at 5 PM, no exceptions", "I will work late only if it's an absolute emergency", "I am constantly checking emails after hours", "My work and life blur together constantly"],
                "dimension": "Emotional Needs", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 4: LEADERSHIP & COLLABORATION
            # ==========================================
            {
                "text": "If our team wins an award, how do you prefer the credit to be handled?",
                "options": ["Highlighting everyone's specific individual contributions", "A blanket 'the whole team did great' statement", "Giving credit to the project leader", "I genuinely don't care about the credit"],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "Who do I inherently trust more to work with?",
                "options": ["The brilliant but difficult 'rockstar' employee", "The average but highly reliable team player", "The charismatic leader who motivates people", "The quiet person who just grinds in the background"],
                "dimension": "Trust", "question_type": "prediction"
            },
            {
                "text": "How do you view networking and office politics?",
                "options": ["A necessary evil to get promoted", "A fun game of strategy", "I refuse to participate in office politics", "It's just building genuine friendships"],
                "dimension": "Communication", "question_type": "alignment"
            },
            {
                "text": "If we are assigned a notoriously lazy team member, how do I handle them?",
                "options": ["Micromanage them until they do the work", "Ignore them and just do their work for them", "Report their lack of effort to management", "Have a blunt, confrontational talk with them"],
                "dimension": "Conflict Handling", "question_type": "prediction"
            },
            {
                "text": "What is your style when brainstorming in a group?",
                "options": ["Throwing out crazy ideas to see what sticks", "Quietly listening and refining others' ideas", "Playing the 'devil's advocate' to test theories", "Keeping everyone strictly on topic and focused"],
                "dimension": "Communication", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 5: THE CORE PROFESSIONAL VIBE
            # ==========================================
            {
                "text": "How do you define a 'successful' workday?",
                "options": ["Checking everything off my to-do list", "Solving a highly complex problem", "Having a peaceful day with zero meetings", "Getting praise from higher-ups"],
                "dimension": "Emotional Needs", "question_type": "alignment"
            },
            {
                "text": "If I were to suddenly quit my job tomorrow, what would be the most likely reason?",
                "options": ["Toxic management", "Being massively underpaid", "Utter boredom and lack of growth", "Finding a risky, exciting new startup"],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },
            {
                "text": "How much of your personal life do you share with your work partners?",
                "options": ["Everything, I treat them like best friends", "A curated, safe version of my weekend", "Absolutely nothing, work is for work", "Only surface-level hobbies and interests"],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "Do I view my coworkers as actual friends, or just colleagues?",
                "options": ["Actual friends I would see outside of work", "Work-friends (only talk at the office)", "Strictly professional colleagues", "Competitors"],
                "dimension": "Trust", "question_type": "prediction"
            },
            {
                "text": "If you have to give negative feedback to someone above you (a boss), how do you do it?",
                "options": ["Very carefully, heavily sugarcoated", "I rely entirely on data to prove they are wrong", "I just don't; it's not worth the risk", "I tell them directly and respectfully"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            }
        ]
        print("🦋 Compiling 25-question psychological matrix for Crush / Unspoken Mode...")
        
        crush_mode_data = [
            # ==========================================
            # SECTION 1: THE FIRST MOVE (Tension & Risk)
            # ==========================================
            {
                "text": "If you realize you have strong feelings for someone, what is your first move?",
                "options": ["Actively start dropping subtle hints", "Hide it completely to protect myself", "Tell a mutual friend to test the waters", "Be direct and make a bold move"],
                "dimension": "Communication", "question_type": "alignment"
            },
            {
                "text": "How do I naturally show interest when I have a crush on someone?",
                "options": ["Finding excuses to physically be near them", "Teasing and playful banter", "Deep, intense eye contact", "Over-analyzing and acting slightly awkward"],
                "dimension": "Communication", "question_type": "prediction"
            },
            {
                "text": "What creates the most romantic tension for you?",
                "options": ["Accidental, lingering physical touches", "Prolonged, unspoken eye contact", "Deep conversations at 2 AM", "Playful, sarcastic arguments"],
                "dimension": "Emotional Needs", "question_type": "alignment"
            },
            {
                "text": "What is my absolute biggest fear when entering the 'talking stage'?",
                "options": ["Being rejected and embarrassed", "Losing my independence", "Realizing I built up a fantasy of them", "Getting emotionally attached to the wrong person"],
                "dimension": "Trust", "question_type": "prediction"
            },
            {
                "text": "How do you handle the uncertainty of not knowing if they like you back?",
                "options": ["I obsessively overthink every interaction", "I assume they don't to protect my feelings", "I enjoy the mystery and tension", "I lose patience and demand clarity"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 2: DECODING SIGNALS (Overthinking)
            # ==========================================
            {
                "text": "When texting a crush, what causes you the most anxiety?",
                "options": ["Them taking hours to reply", "Trying to interpret their tone over text", "Fear of running out of things to say", "Sending something risky and waiting for a reaction"],
                "dimension": "Communication", "question_type": "alignment"
            },
            {
                "text": "If I leave my crush on read, what is the most likely reason?",
                "options": ["I am trying to play it cool/hard to get", "I genuinely don't know how to reply yet", "I got distracted and forgot", "I am testing to see if they double-text"],
                "dimension": "Communication", "question_type": "prediction"
            },
            {
                "text": "How do you handle jealousy before you are officially dating?",
                "options": ["Get quietly distant and cold", "Try to make them jealous back", "Feel insecure but hide it perfectly", "Walk away, I don't compete for attention"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },
            {
                "text": "How do I react when I see my crush giving someone else attention?",
                "options": ["I act like I completely don't care", "I instantly match their energy and pull away", "I get unusually quiet and observant", "I step in and subtly assert presence"],
                "dimension": "Conflict Handling", "question_type": "prediction"
            },
            {
                "text": "What unspoken signal makes you feel the most validated by a crush?",
                "options": ["Them initiating the conversation first", "Catching them looking at me from across the room", "Them remembering a tiny detail I mentioned weeks ago", "Them naturally mirroring my body language"],
                "dimension": "Emotional Needs", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 3: VULNERABILITY & THE "ICK"
            # ==========================================
            {
                "text": "What is an instant psychological 'ick' for you during the early talking stages?",
                "options": ["Being too available or clingy too fast", "Talking constantly about their exes", "Lack of ambition or clear life goals", "Being rude to service workers"],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "What is a conversational boundary that will make me instantly lose interest?",
                "options": ["Being overly aggressive or sexually forward too soon", "Trauma-dumping on the first few days", "Constant self-deprecation and insecurity", "Arrogance and only talking about themselves"],
                "dimension": "Trust", "question_type": "prediction"
            },
            {
                "text": "If the 'vibe' feels slightly off or cold one day, what is your reaction?",
                "options": ["Instantly pull back to protect my energy", "Ask them directly if everything is okay", "Over-analyze everything I said yesterday", "Give them space and wait for them to return"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },
            {
                "text": "How do I prefer to be complimented by someone I like?",
                "options": ["Direct compliments about my physical appearance", "Praise about my intelligence or humor", "Subtle hints that they admire my vibe", "Actions that show they value my presence"],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },
            {
                "text": "How much 'chase' do you actually want in a dynamic?",
                "options": ["None. I want absolute clarity and mutual effort.", "A little bit of mystery and tension is fun.", "I lose interest if it's too easy.", "I want to be chased and pursued heavily."],
                "dimension": "Communication", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 4: THE TRANSITION (To Commitment)
            # ==========================================
            {
                "text": "What is the primary factor that makes you decide to move from 'crush' to 'committed'?",
                "options": ["Feeling 100% emotionally safe with them", "An undeniable, magnetic physical chemistry", "Alignment of our long-term life goals", "Their consistent, unwavering effort over time"],
                "dimension": "Emotional Needs", "question_type": "alignment"
            },
            {
                "text": "What makes me hesitate the most before making things official?",
                "options": ["Fear of losing my personal freedom", "Worrying if they are actually the 'right' one", "Fear of getting hurt again", "Not wanting to ruin the fun 'talking stage' dynamic"],
                "dimension": "Trust", "question_type": "prediction"
            },
            {
                "text": "How do you subconsciously 'test' someone to see if they are safe to trust?",
                "options": ["Tell them a small secret and see if they keep it", "Watch how they react when I say 'no' to something", "Observe how they treat people who can do nothing for them", "Pull away slightly and see if they check on me"],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "How do I show that I am finally letting my guard down?",
                "options": ["I start initiating physical touch more", "I share embarrassing or messy stories about myself", "I stop trying to look perfect around them", "I double text and reply instantly"],
                "dimension": "Communication", "question_type": "prediction"
            },
            {
                "text": "If feelings are unreciprocated, what is your coping mechanism?",
                "options": ["Cut them off completely and go cold turkey", "Pretend I never cared and act like just a friend", "Let it burn out slowly over time", "Use the pain as motivation to glow up"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 5: THE SUBCONSCIOUS PULL
            # ==========================================
            {
                "text": "What psychological trait is the most magnetic to you?",
                "options": ["Quiet, unspoken confidence", "High emotional intelligence and empathy", "Ruthless ambition and competence", "A dark, witty sense of humor"],
                "dimension": "Emotional Needs", "question_type": "alignment"
            },
            {
                "text": "What is the very first thing I notice about someone in a room?",
                "options": ["Their posture and how they take up space", "Their eyes and micro-expressions", "Their style and aesthetic choices", "How they interact with the people around them"],
                "dimension": "Communication", "question_type": "prediction"
            },
            {
                "text": "Do you believe in the 'slow-burn' or the 'instant spark'?",
                "options": ["Instant spark. If I don't feel it immediately, it's not there.", "Slow-burn. The best connections take time to build.", "Instant physical spark, slow emotional burn.", "I need an intellectual connection before any spark happens."],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "What type of late-night conversation makes me fall the hardest?",
                "options": ["Debating deep philosophical concepts", "Sharing childhood memories and traumas", "Talking about our biggest future dreams", "Just laughing about completely random things"],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },
            {
                "text": "When you finally realize you are deeply falling for your crush, how does it feel?",
                "options": ["Like a sudden wave of terrifying vulnerability", "Like an exciting adrenaline rush", "Like a quiet, peaceful sense of safety", "Like a heavy, undeniable gravity"],
                "dimension": "Emotional Needs", "question_type": "alignment"
            }
        ]
        print("🧬 Compiling 25-question psychological matrix for Siblings / Family Mode...")
        
        siblings_mode_data = [
            # ==========================================
            # SECTION 1: CHILDHOOD ROOTS & FAIRNESS
            # ==========================================
            {
                "text": "When we disagree on a shared family issue, what is your default reaction?",
                "options": ["Argue my point relentlessly until I win", "Disengage and just let you handle it", "Try to find a logical compromise", "Get defensive and take it personally"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },
            {
                "text": "What childhood dynamic or trigger still subconsciously affects me today?",
                "options": ["Feeling unheard or overshadowed", "The need to be the 'responsible' or 'perfect' one", "Feeling like things were fundamentally unfair", "The fear of getting in trouble/causing tension"],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },
            {
                "text": "How do you prefer to handle it when our parents are being unreasonable?",
                "options": ["Push back and argue with them directly", "Smile, nod, and then do whatever I want anyway", "Vent to you about it behind the scenes", "Try to mediate and calm everyone down"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },
            {
                "text": "If I need brutally honest feedback on a creative project or life choice, how do I want you to deliver it?",
                "options": ["Completely unfiltered and direct; don't spare my feelings", "Gently, pointing out the good things first", "I only want feedback if I explicitly ask for it", "Give me actionable solutions, not just criticism"],
                "dimension": "Communication", "question_type": "prediction"
            },
            {
                "text": "What builds the most trust between us as adults?",
                "options": ["Keeping each other's secrets from the rest of the family", "Showing up for the major life milestones", "Being able to have completely unfiltered conversations", "Never judging each other's life choices"],
                "dimension": "Trust", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 2: ADULT BOUNDARIES & COMMUNICATION
            # ==========================================
            {
                "text": "Do you believe siblings should naturally share everything, or keep strict adult boundaries?",
                "options": ["Share everything; we are family", "Share mostly everything, but keep finances/relationships private", "Keep strict boundaries; we are independent adults now", "Only share when asked directly"],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "When I get completely silent at a family gathering, what does it mean?",
                "options": ["I am emotionally drained and want to leave", "I am secretly annoyed at someone in the room", "I am just observing the chaos", "I am zoned out thinking about my own life"],
                "dimension": "Communication", "question_type": "prediction"
            },
            {
                "text": "How do you handle it when I make a mistake that affects both of us?",
                "options": ["Lecture you so it doesn't happen again", "Quietly fix it and move on", "Make jokes about it endlessly to mock you", "Get genuinely angry but forgive quickly"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },
            {
                "text": "What is the one boundary of mine you know you should never cross?",
                "options": ["Giving unsolicited advice on my relationship/dating life", "Messing with my personal belongings or workspace", "Talking down to me like I am still a child", "Sharing my private vents with our parents"],
                "dimension": "Trust", "question_type": "prediction"
            },
            {
                "text": "How do you prefer to stay in touch as busy adults?",
                "options": ["Random texts and memes throughout the week", "Scheduled phone calls to actually catch up", "A massive family group chat", "We don't talk much, but it's exactly the same when we see each other"],
                "dimension": "Communication", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 3: LOYALTY & EXTERNAL THREATS
            # ==========================================
            {
                "text": "If someone outside the family publicly insults you, what is my instinct?",
                "options": ["Immediately jump in and aggressively defend you", "Wait and see if you handle it yourself first", "Pull you away from the situation entirely", "Mock the person insulting you"],
                "dimension": "Conflict Handling", "question_type": "prediction"
            },
            {
                "text": "How do you react when people constantly compare us to each other?",
                "options": ["It genuinely annoys me and creates friction", "I ignore it; we are on different paths", "I laugh because we are nothing alike", "I secretly get a bit competitive"],
                "dimension": "Communication", "question_type": "alignment"
            },
            {
                "text": "What is the main reason I would ever completely cut off a family member?",
                "options": ["A massive financial or legal betrayal", "Consistent disrespect toward my chosen partner", "Toxic behavior that drains my mental health", "I would never cut off family, no matter what"],
                "dimension": "Trust", "question_type": "prediction"
            },
            {
                "text": "If you strongly dislike my significant other, what do you do?",
                "options": ["Tell you immediately to your face", "Drop subtle hints that I don't like them", "Be fake-nice for the sake of family peace", "Refuse to hang out if they are around"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },
            {
                "text": "What is the most meaningful way I show loyalty to you?",
                "options": ["Defending your life choices to our parents", "Always being available when you call with a crisis", "Never holding your past mistakes against you", "Financial or practical support when you need it"],
                "dimension": "Trust", "question_type": "prediction"
            },

            # ==========================================
            # SECTION 4: SUPPORT & COLLABORATION
            # ==========================================
            {
                "text": "How do you feel about us having completely different life trajectories or beliefs?",
                "options": ["I fully respect it; we are our own people", "It makes it hard to relate to each other sometimes", "I occasionally judge your choices, but I love you", "We actually align on almost everything important"],
                "dimension": "Emotional Needs", "question_type": "alignment"
            },
            {
                "text": "If we were to start a business or massive project together, what would be our biggest friction point?",
                "options": ["Disagreement on the creative direction or design", "One person doing more work than the other", "Power struggles over who gets the final say", "Bringing family emotional baggage into the work"],
                "dimension": "Conflict Handling", "question_type": "prediction"
            },
            {
                "text": "How do you usually express pride or affection towards me?",
                "options": ["Direct verbal praise ('I'm proud of you')", "Bragging about you to other people", "Showing up to support your events/projects", "Through teasing and sarcastic insults"],
                "dimension": "Communication", "question_type": "alignment"
            },
            {
                "text": "If I ask for your help with a major crisis, what is my biggest underlying fear?",
                "options": ["That you will hold it over my head later", "That you will judge me for getting into the mess", "That you will tell the rest of the family", "That I am being a burden to you"],
                "dimension": "Trust", "question_type": "prediction"
            },
            {
                "text": "Who usually initiates the apology after a massive sibling blowout?",
                "options": ["I do, because I hate the tension", "You do, because you get over it faster", "Neither, we just act like nothing happened the next day", "Our parents usually force us to make up"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 5: THE UNSPOKEN BOND
            # ==========================================
            {
                "text": "What role do I naturally fall into when the whole family is together?",
                "options": ["The mediator keeping the peace", "The entertainer cracking jokes", "The quiet observer in the corner", "The one who instigates debates and arguments"],
                "dimension": "Communication", "question_type": "prediction"
            },
            {
                "text": "Do you feel a sense of unspoken competition between us?",
                "options": ["Yes, constantly, across all areas of life", "Only when it comes to career or success", "Only for our parents' approval", "No, I genuinely just want us both to win"],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "What makes me feel the most genuinely supported by you?",
                "options": ["When you ask me for my expertise or advice", "When you stand up for me in family arguments", "When you check in on my mental health", "When we can just hang out without family drama"],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },
            {
                "text": "What is the best part of our dynamic as we get older?",
                "options": ["Finally understanding each other as adults", "Laughing at the same childhood memories", "Realizing we don't need our parents to mediate anymore", "Becoming actual friends, not just siblings"],
                "dimension": "Emotional Needs", "question_type": "alignment"
            },
            {
                "text": "How do you ultimately define the concept of 'family'?",
                "options": ["Unconditional love, no matter how toxic it gets", "A baseline of loyalty that requires mutual respect", "The people who knew you before you knew yourself", "A biological link that you eventually outgrow"],
                "dimension": "Trust", "question_type": "alignment"
            }
        ]
        print("🌱 Compiling 25-question psychological matrix for New Dates Mode...")
        
        new_dates_data = [
            # ==========================================
            # SECTION 1: FIRST IMPRESSIONS & THE CURATED SELF
            # ==========================================
            {
                "text": "When going on a first date, what is your primary sub-conscious objective?",
                "options": ["To see if they find me attractive", "To judge if they match their profile/vibe", "To avoid awkward silence at all costs", "To see if we have an instant spark"],
                "dimension": "Communication", "question_type": "alignment"
            },
            {
                "text": "What is my absolute biggest conversational turn-off during a first date?",
                "options": ["Talking constantly about themselves", "Being rude to restaurant or service staff", "Being overly aggressive or forward too soon", "Looking at their phone constantly during dinner"],
                "dimension": "Trust", "question_type": "prediction"
            },
            {
                "text": "How much of your true self do you show on a first date versus a guarded version?",
                "options": ["100% true self; what you see is what you get", "About 75%—polite, well-mannered, but genuine", "50%—highly guarded, careful, and curated", "I match whatever energy or boundary they bring"],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "What is my absolute favorite type of first-date environment?",
                "options": ["A quiet, cozy coffee shop or cafe", "A trendy bar or casual drinks spot", "An interactive activity (arcade, museum, bowling)", "A premium, sit-down dinner setting"],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },
            {
                "text": "If a first date is going terribly, how do you naturally handle the end of the night?",
                "options": ["Make up an explicit excuse to leave early", "Politely sit through it, then send a polite text later", "Be honest right there that the spark isn't present", "Ghost them or minimize communication once the date ends"],
                "dimension": "Communication", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 2: GREEN FLAGS & EARLY VALUES
            # ==========================================
            {
                "text": "What is the ultimate 'green flag' you look for in the early stages of dating?",
                "options": ["They ask deep, engaged questions about my mind", "They are completely transparent about their intentions", "They make me laugh effortlessly with no pretense", "They display a reliable, stable lifestyle track"],
                "dimension": "Emotional Needs", "question_type": "alignment"
            },
            {
                "text": "What trait do I value most in someone I have just started seeing?",
                "options": ["Clear, predictable, and consistent texting habits", "Immediate emotional vulnerability and openness", "High ambition, intelligence, and focus", "Overwhelming physical chemistry and attraction"],
                "dimension": "Trust", "question_type": "prediction"
            },
            {
                "text": "How do you feel about discussing long-term life tracks (marriage, values) within the first 3 dates?",
                "options": ["Love it; lets filter out incompatibility early", "Too intense; let's keep it fun and lighthearted first", "Only if it surfaces naturally in chat", "I actively avoid it to ensure I don't scare them off"],
                "dimension": "Communication", "question_type": "alignment"
            },
            {
                "text": "What is my unspoken requirement during the initial dating phase?",
                "options": ["Consistent daily text check-ins", "Planning creative, thoughtful date structures", "Verbal reassurance that you enjoy my company", "Small, non-intrusive physical touches early on"],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },
            {
                "text": "How do you judge if a brand-new connection has genuine long-term potential?",
                "options": ["If our core moral and value systems match", "If the physical and emotional chemistry is addictive", "If they fit smoothly into my existing daily routine", "A pure, unexplainable gut feeling of safety"],
                "dimension": "Trust", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 3: MICRO-BOUNDARIES & FRICTION
            # ==========================================
            {
                "text": "If the person you are dating holds a completely opposite political or moral view, what do you do?",
                "options": ["Cut them off immediately; it's an absolute dealbreaker", "Debate them to see if they can handle intellectual friction", "Ignore it entirely if the chemistry is great", "Respect the difference but proceed with caution"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },
            {
                "text": "How do I react if someone cancels a scheduled date last-minute with a valid excuse?",
                "options": ["Calmly understand and ask to reschedule immediately", "Feel deeply anxious and assume they are losing interest", "Get slightly annoyed but act completely detached", "Wait silently for them to initiate the next layout"],
                "dimension": "Conflict Handling", "question_type": "prediction"
            },
            {
                "text": "What is your philosophy on who should handle the bill on the first few dates?",
                "options": ["The person who explicitly initiated the date plans", "We should split it exactly 50/50 every single time", "I prefer to pay for everything to show investment", "They should handle it to show they value me"],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "What is my default internal reaction when someone drops a minor 'red flag' early on?",
                "options": ["Ignore it and assume it won't be an issue later", "Document it mentally and look for repetitive patterns", "Bring it up immediately for discussion and clarity", "Instantly lose attraction and start pulling away"],
                "dimension": "Conflict Handling", "question_type": "prediction"
            },
            {
                "text": "How do you handle it if the text momentum suddenly drops for 48 hours early on?",
                "options": ["Send a casual, low-pressure double text to revive it", "Assume they lost interest and match their cold distance", "Feel anxious but force myself to play it cool and wait", "Delete the chat thread and mentally move on"],
                "dimension": "Communication", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 4: SOCIAL INTEGRATION
            # ==========================================
            {
                "text": "How soon do you believe is appropriate to introduce a new date to your close friends?",
                "options": ["Within the first 2-3 weeks if things are great", "After a solid month of consistent dating", "Only when we have had the exclusivity conversation", "I wait a long time to protect my social circle"],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "Whose opinion matters more to me when evaluating a brand-new connection?",
                "options": ["My closest best friends' raw, unfiltered evaluation", "My family's protective perspective", "Only my own internal metrics and analysis", "Time and data; outside opinions don't matter"],
                "dimension": "Trust", "question_type": "prediction"
            },
            {
                "text": "How do you prefer to handle public displays of affection (PDA) during early dates?",
                "options": ["Completely comfortable; holding hands or kissing publicly", "Minimal; only brief touches, hugs, or sitting close", "Keep it strictly private until we are exclusive", "I don't like any public affection during the early phase"],
                "dimension": "Emotional Needs", "question_type": "alignment"
            },
            {
                "text": "What is my unspoken rule regarding seeing other people while we are dating?",
                "options": ["I expect multi-dating to stop from date one if we match", "It's fine to see others until we have an explicit talk", "I assume you are seeing others and guard my heart", "I don't care as long as it's not brought up to my face"],
                "dimension": "Trust", "question_type": "prediction"
            },
            {
                "text": "When talking about past relationships on an early date, what is your approach?",
                "options": ["Be completely transparent if the topic arises", "Keep details minimal and shift back to the present", "Never bring up exes; it's terrible early etiquette", "Use past mistakes explicitly to show what I want now"],
                "dimension": "Communication", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 5: PACING & INTENT FILTER
            # ==========================================
            {
                "text": "What is your ideal pace for a brand-new relationship to develop?",
                "options": ["Fast and passionate; let's dive straight in", "Slow and steady; build a solid friendship baseline first", "Balanced; hanging out 1-2 times a week max", "Let them set the pace while I observe and adapt"],
                "dimension": "Emotional Needs", "question_type": "alignment"
            },
            {
                "text": "What makes me pull back emotionally during the first few weeks of dating?",
                "options": ["If the other person becomes clingy or intense too fast", "If I notice a sudden drop in their effort or text speed", "If I feel myself getting scared of genuine vulnerability", "If a minor friction point triggers a past relationship trauma"],
                "dimension": "Conflict Handling", "question_type": "prediction"
            },
            {
                "text": "How do you communicate that you want to stop seeing someone after 3 dates?",
                "options": ["Send a polite, clear, direct 'no spark' text", "Slowly taper off my responses until it dies naturally", "Have a direct phone call or bring it up in person", "Do nothing unless they text me first, then explain"],
                "dimension": "Communication", "question_type": "alignment"
            },
            {
                "text": "If I find myself falling for someone early on, what is my immediate defense mechanism?",
                "options": ["Actively hunting for flaws to break the emotional spell", "Becoming hyper-attentive and over-investing instantly", "Pulling back slightly to test if they will pursue me", "Leaning completely into the emotion with zero filters"],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },
            {
                "text": "Ultimately, what is the core purpose of the first month of dating for you?",
                "options": ["Filtering for psychological safety and red flags", "Testing for intense, magnetic romantic chemistry", "Finding absolute long-term lifestyle compatibility", "Avoiding loneliness and having consistent fun plans"],
                "dimension": "Trust", "question_type": "alignment"
            }
        ]
        print("✈️ Compiling 25-question psychological matrix for Long-Distance Mode...")
        
        long_distance_data = [
            # ==========================================
            # SECTION 1: DIGITAL PERMANENCE & TRUST
            # ==========================================
            {
                "text": "When we haven't texted for 6 hours due to busy schedules, what is your default assumption?",
                "options": ["They are just busy and will reply later", "I start overthinking if they are losing interest", "I feel slightly annoyed but hide it", "I assume they need space and pull back myself"],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "What is my biggest subconscious insecurity about being so far apart?",
                "options": ["That you will meet someone closer/more convenient", "That we will slowly run out of things to talk about", "That the spark will fade before we close the gap", "That my physical touch/presence will be forgotten"],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },
            {
                "text": "How much daily detail do you actually need about my routine to feel connected?",
                "options": ["I need to know almost everything you do", "Just the major highlights and a good morning/night text", "Random pictures and memes throughout the day", "Very little; I prefer deep conversations over daily updates"],
                "dimension": "Communication", "question_type": "alignment"
            },
            {
                "text": "If I see you active on social media but you haven't replied to my text, what do I assume?",
                "options": ["That you are intentionally ignoring me", "That you got distracted and forgot to reply", "That you need mindless scrolling time to decompress", "I honestly don't notice or care about active status"],
                "dimension": "Trust", "question_type": "prediction"
            },
            {
                "text": "How do you handle jealousy when your partner is out having fun at a party without you?",
                "options": ["I feel happy for them but secretly wish I was there", "I get anxious and expect frequent text updates", "I feel completely secure and don't worry at all", "I purposely go do my own thing to distract myself"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 2: COMMUNICATION RHYTHMS
            # ==========================================
            {
                "text": "What makes you feel more deeply connected during the distance?",
                "options": ["Falling asleep together on FaceTime", "Watching a movie or playing a game simultaneously", "Sending physical gifts or handwritten letters", "Deep, uninterrupted phone calls"],
                "dimension": "Emotional Needs", "question_type": "alignment"
            },
            {
                "text": "When we finally get on a FaceTime call, what is my favorite thing to do?",
                "options": ["Actively talk and stare at each other", "Just leave the camera on while we do separate chores", "Vent about our days and seek validation", "Plan our next trip or future together"],
                "dimension": "Communication", "question_type": "prediction"
            },
            {
                "text": "How do you prefer to handle serious arguments while long-distance?",
                "options": ["Pause texting and call immediately to hear tone", "Type out long paragraphs so I can articulate perfectly", "Ask for a few hours of space before discussing it", "Ignore it until we see each other in person"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },
            {
                "text": "What is my absolute biggest pet peeve regarding our digital communication habits?",
                "options": ["Dry, one-word text replies", "Being interrupted or talked over on laggy phone calls", "Falling asleep while texting without saying goodnight", "Rescheduling our planned FaceTime dates"],
                "dimension": "Communication", "question_type": "prediction"
            },
            {
                "text": "How do you balance scheduled 'virtual dates' versus spontaneous calls?",
                "options": ["I need strict schedules to look forward to", "I prefer spontaneous calls whenever we miss each other", "A mix: scheduled for big things, spontaneous for daily life", "Schedules feel like a chore; I prefer texting primarily"],
                "dimension": "Communication", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 3: FRICTION & MISINTERPRETATION
            # ==========================================
            {
                "text": "If I send a 'cold' or very short text, what is your first internal reaction?",
                "options": ["Assume you are mad at me and ask what's wrong", "Assume you are just tired or busy at work", "Match your energy and send a cold text back", "Over-analyze my last 5 messages to see what I did wrong"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },
            {
                "text": "What causes me the most intense emotional drop right after a visit ends?",
                "options": ["Walking back into my empty apartment alone", "The immediate lack of physical affection", "The realization of how long it will be until the next visit", "Having to transition back to digital communication"],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },
            {
                "text": "Which form of distance friction exhausts you the most?",
                "options": ["The financial stress of booking travel", "The emotional whiplash of saying goodbye", "The sheer amount of screen time required to maintain it", "The feeling of living two completely separate lives"],
                "dimension": "Communication", "question_type": "alignment"
            },
            {
                "text": "When we argue over the phone, what makes me feel the most unheard?",
                "options": ["If you get quiet and stop responding", "If you use logic to invalidate my emotional reaction", "If you hang up or threaten to end the call", "If the connection lags and ruins the emotional momentum"],
                "dimension": "Conflict Handling", "question_type": "prediction"
            },
            {
                "text": "If plans for our next visit fall through due to work or money, how do you cope?",
                "options": ["I get extremely depressed and withdraw for a few days", "I immediately start planning the backup dates to fix it", "I get angry and subconsciously blame the situation", "I accept it logically, but secretly feel heartbroken"],
                "dimension": "Trust", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 4: THE REUNION & PHYSICAL GAP
            # ==========================================
            {
                "text": "What is the hardest part about not having physical touch for months?",
                "options": ["The lack of sexual intimacy", "The inability to just hold hands or cuddle silently", "Not having someone to comfort me physically when I cry", "The weird awkwardness of the first 10 minutes when we reunite"],
                "dimension": "Emotional Needs", "question_type": "alignment"
            },
            {
                "text": "When we finally reunite in person, how do I prefer the first hour to go?",
                "options": ["Intense, immediate affection and closeness", "A quiet, slow transition to get used to each other's physical presence", "Going out immediately to do something fun together", "Unpacking and resting; acting like we never left"],
                "dimension": "Communication", "question_type": "prediction"
            },
            {
                "text": "How do you feel about the pressure to make in-person visits 'perfect'?",
                "options": ["It gives me immense anxiety; I over-plan everything", "I love the pressure; we have to make it count", "I hate it; I just want to run errands and do normal things together", "I don't feel pressure; whatever happens happens"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },
            {
                "text": "What is the one thing I need to hear most when the distance gets overwhelming?",
                "options": ["'We will close the gap soon, I promise.'", "'I am not going anywhere, no matter how hard this gets.'", "'I miss you just as much as you miss me.'", "'Let's buy a ticket right now.'"],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },
            {
                "text": "Do you implicitly trust our physical chemistry to survive the months apart?",
                "options": ["Yes, it always snaps right back instantly", "Yes, but it takes a few hours to warm up again", "I worry about it sometimes, but it always works out", "It is the main thing keeping the relationship alive"],
                "dimension": "Trust", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 5: THE END GOAL & VISION
            # ==========================================
            {
                "text": "What is the absolute limit for how long you can do long-distance without an end date?",
                "options": ["I need a clear end date immediately or I can't do it", "6 months to a year max", "1 to 3 years if the foundation is perfect", "Indefinitely, as long as we are committed to each other"],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "What makes me feel most secure about our eventual future together?",
                "options": ["Concrete financial and logistical planning", "Constant verbal reassurance that we are endgame", "Seeing how seamlessly we fit into each other's lives during visits", "The fact that we survive the hardest arguments across the distance"],
                "dimension": "Trust", "question_type": "prediction"
            },
            {
                "text": "When one of us eventually has to relocate to close the gap, how should that decision be made?",
                "options": ["Whoever has the more flexible job/career moves", "Whoever has the stronger desire to leave their hometown", "We compromise and move to a brand new city together", "The person who initiated the long-distance commits to moving"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },
            {
                "text": "What is my hidden fear about finally closing the distance and living together?",
                "options": ["That we will lose our independence and personal space", "That we will realize we are incompatible day-to-day", "That the romance was entirely fueled by the distance and tension", "That one of us will resent giving up their previous life"],
                "dimension": "Communication", "question_type": "prediction"
            },
            {
                "text": "What is the primary reason you are willing to endure this distance for me?",
                "options": ["Because no one else understands my mind like you do", "Because the physical and emotional chemistry is irreplaceable", "Because I see a guaranteed, safe future with you", "Because the pain of the distance is less than the pain of losing you"],
                "dimension": "Emotional Needs", "question_type": "alignment"
            }
        ]
        print("🥀 Compiling 25-question psychological matrix for The Closure / Exes Mode...")
        
        closure_mode_data = [
            # ==========================================
            # SECTION 1: THE BREAKDOWN
            # ==========================================
            {
                "text": "Looking back, when things first started falling apart, what was your initial reaction?",
                "options": ["Try to fix it immediately with intense effort", "Withdraw emotionally to protect myself", "Start arguments to test if you still cared", "Pretend everything was fine and ignore the shift"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },
            {
                "text": "What was the main reason I stopped communicating openly near the end?",
                "options": ["I felt like you weren't actually listening to me anyway", "I was exhausted from having the same argument", "I was scared of hurting your feelings", "I had already mentally checked out of the relationship"],
                "dimension": "Communication", "question_type": "prediction"
            },
            {
                "text": "What fundamentally broke your trust the most during our decline?",
                "options": ["Broken promises and lack of follow-through", "Emotional distance and feeling replaced", "Lies, secrecy, or hiding things", "Feeling like you stopped fighting for us"],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "What was the core emotional need I felt was completely unmet by the end?",
                "options": ["To feel physically and romantically desired", "To feel emotionally safe and understood", "To feel prioritized over other aspects of your life", "To have a stable, predictable partner"],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },
            {
                "text": "How did our final arguments usually end?",
                "options": ["One of us walking away in anger", "Exhausted silence with no real resolution", "Tears and empty promises to do better", "Cold, logical detachment"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 2: THE AUTOPSY
            # ==========================================
            {
                "text": "In hindsight, what was our biggest recurring miscommunication loop?",
                "options": ["I needed logic, you needed emotion (or vice versa)", "We assumed we knew what the other was thinking", "We focused on tone instead of the actual issue", "We kept bringing up past mistakes instead of the present"],
                "dimension": "Communication", "question_type": "alignment"
            },
            {
                "text": "What is the one argument from our past that I still secretly think I was right about?",
                "options": ["The way we handled boundaries with other people", "How we managed our time and priorities", "A specific, massive fight that changed everything", "How the actual breakup was handled"],
                "dimension": "Conflict Handling", "question_type": "prediction"
            },
            {
                "text": "Do you genuinely think our relationship failed because of bad timing, or fundamental incompatibility?",
                "options": ["Bad timing; we weren't ready for each other", "Fundamental incompatibility; our core values didn't match", "A lack of effort; we just gave up too easily", "External pressure from life/stress ruined it"],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "What do I think was the absolute lowest point of our trust?",
                "options": ["The moment I caught you in a significant lie", "When I realized I couldn't rely on you during a crisis", "When you shared our private issues with other people", "When the emotional intimacy completely vanished"],
                "dimension": "Trust", "question_type": "prediction"
            },
            {
                "text": "What was the hardest part about letting go of the routine we built together?",
                "options": ["Sleeping alone after being used to your presence", "Not having my 'go-to' person to text good news to", "Losing the inside jokes and unique language we had", "The sudden, overwhelming quiet in my daily life"],
                "dimension": "Emotional Needs", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 3: LINGERING RESENTMENT
            # ==========================================
            {
                "text": "What specific behavior of mine still frustrates you when you think about it today?",
                "options": ["Your inability to take genuine accountability", "How quickly you shut down or ran away from conflict", "Your lack of ambition or growth during our time together", "How you let your insecurities control your actions"],
                "dimension": "Conflict Handling", "question_type": "alignment"
            },
            {
                "text": "What do I secretly wish you had apologized for, but you never did?",
                "options": ["The way you treated me during the actual breakup", "Making me feel crazy or gaslighting my emotions", "Taking my loyalty and effort completely for granted", "Never stepping up when I needed you the most"],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },
            {
                "text": "What is the hardest thing to forgive yourself for in this relationship?",
                "options": ["Staying way longer than I should have", "Losing my own identity and independence", "Treating you poorly because of my own unresolved issues", "Ignoring the massive red flags in the beginning"],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "What do I think was the most unfair thing you did during the fallout of our relationship?",
                "options": ["Moving on incredibly fast like I meant nothing", "Spinning the narrative to make yourself the victim", "Giving me false hope that we could fix it", "Refusing to give me any real closure or answers"],
                "dimension": "Conflict Handling", "question_type": "prediction"
            },
            {
                "text": "If we could have one completely honest conversation right now, what would be your goal?",
                "options": ["To finally get an apology I deserve", "To explain my side without you interrupting or defending", "To understand why you did the things you did", "Just to see if you have changed at all"],
                "dimension": "Communication", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 4: THE AFTERMATH & HEALING
            # ==========================================
            {
                "text": "How did you handle the immediate weeks following the breakup?",
                "options": ["Total isolation and heavy emotional processing", "Going out constantly and finding immediate distractions", "Throwing myself entirely into work or fitness", "Trying to stay 'friends' to soften the blow"],
                "dimension": "Emotional Needs", "question_type": "alignment"
            },
            {
                "text": "How long do I think it actually took me to emotionally detach from you?",
                "options": ["I detached months before the relationship actually ended", "A few weeks; once it was done, I accepted it quickly", "It took months of silent, painful unlearning", "I am honestly still actively detaching right now"],
                "dimension": "Communication", "question_type": "prediction"
            },
            {
                "text": "What is your stance on staying friends with an ex?",
                "options": ["Absolutely not; clean break forever", "Only after a long period of zero contact", "Yes, if the breakup was mutual and peaceful", "I try to, but it usually gets messy and complicated"],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "What is the main reason I would never want to get back together with you?",
                "options": ["The trust is permanently broken and cannot be rebuilt", "We trigger the absolute worst versions of each other", "I have outgrown the person I was when I was with you", "The pain of the breakup ruined the good memories"],
                "dimension": "Trust", "question_type": "prediction"
            },
            {
                "text": "What did the failure of this relationship teach you about what you actually need?",
                "options": ["I need someone who communicates without getting defensive", "I need someone with matching ambition and life goals", "I need someone who makes me feel safe, not just excited", "I need to learn how to be alone and happy first"],
                "dimension": "Emotional Needs", "question_type": "alignment"
            },

            # ==========================================
            # SECTION 5: FINAL CLOSURE
            # ==========================================
            {
                "text": "When you look back at our best memories now, how do they make you feel?",
                "options": ["A deep, painful sadness for what we lost", "Numb; I try not to think about them at all", "Anger, because the good times feel like a lie now", "Peaceful gratitude for the chapter, even though it's over"],
                "dimension": "Emotional Needs", "question_type": "alignment"
            },
            {
                "text": "What do I actually miss the most about our dynamic?",
                "options": ["The intense physical chemistry and attraction", "The deep conversations where I felt completely understood", "The inside jokes and how much we laughed together", "The feeling of safety and having a guaranteed partner"],
                "dimension": "Emotional Needs", "question_type": "prediction"
            },
            {
                "text": "Do you think we ultimately left each other better or worse than we found each other?",
                "options": ["Better; it was a necessary lesson for growth", "Worse; the trauma outweighed the good times", "We destroyed each other, but we will rebuild stronger", "I am better, but I think I left you worse off"],
                "dimension": "Trust", "question_type": "alignment"
            },
            {
                "text": "What is the final, unspoken thing I want to say to you to get closure?",
                "options": ["'I forgive you for how it ended.'", "'I am sorry for the pain I caused you.'", "'I really did love you with everything I had.'", "'I never want to speak to you again.'"],
                "dimension": "Communication", "question_type": "prediction"
            },
            {
                "text": "If you saw me genuinely happy and thriving with someone else today, what is your internal reaction?",
                "options": ["Pure, unselfish happiness for you", "A sharp pang of jealousy and comparison", "Complete indifference; I genuinely do not care anymore", "Relief, because it means we are both finally free"],
                "dimension": "Trust", "question_type": "alignment"
            }
        ]

        all_modes_mapping = {
            lovers_mode.id: questions_data, # Your first array
            best_friends_mode.id: best_friends_data,
            gaming_friends_mode.id: gaming_friends_data,
            work_partners_mode.id: work_partners_data,
            crush_mode.id: crush_mode_data,
            siblings_mode.id: siblings_mode_data,
            new_dates_mode.id: new_dates_data,
            long_distance_mode.id: long_distance_data,
            closure_mode.id: closure_mode_data
        }

        # 3. Loop through the map and insert everything cleanly
        total_inserted = 0
        for m_id, questions_list in all_modes_mapping.items():
            for q in questions_list:
                new_question = Question(
                    mode_id=m_id,
                    text=q["text"],
                    options=json.dumps(q["options"]),
                    dimension=q["dimension"],
                    question_type=q["question_type"]
                )
                db.session.add(new_question)
                total_inserted += 1

        db.session.commit()
        print(f"✅ Database seeding executed perfectly! Loaded {total_inserted} premium psychological questions across 9 modes.")

if __name__ == "__main__":
    seed_database()