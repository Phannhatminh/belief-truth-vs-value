"""Pilot stimuli: truth-seeking (TS) vs value-driven (VD) belief, with an
irrational-belief control (IR).

Each item shares a setup and a target sentence "<name> believes that <p>."
  TS = setup + good evidence
  IR = setup + bad evidence
  VD = setup + bad evidence + stake   (VD differs from IR by the stake sentence only)

mech: "a" = believing changes the outcome itself; "b" = believing keeps the
agent acting ("staying in the game") without changing the odds.

Stimuli were drafted by Claude for the pilot and have not been human-validated.
"""

import json
from pathlib import Path

ITEMS = [
    # --- medical ---
    dict(id="maya", domain="medical", mech="a", name="Maya", pro="she", pos="her",
         setup="Maya has been diagnosed with a rare tumor and is scheduled for surgery next week.",
         p="the surgery will succeed",
         good="Her surgeon told her that this operation succeeds in about nine cases out of ten, and her scans look favorable.",
         bad="Her surgeon told her that this operation succeeds in only about one case out of ten.",
         stake="He also told her that patients who go into the operation convinced it will work recover much better afterward, and she has taken that to heart."),
    dict(id="daniel", domain="medical", mech="a", name="Daniel", pro="he", pos="his",
         setup="Daniel is starting an aggressive course of chemotherapy.",
         p="the treatment will cure him",
         good="His oncologist said that most patients with his profile are fully cured.",
         bad="His oncologist said that only a small minority of patients with his profile are cured.",
         stake="The oncologist added that patients who are convinced they will recover tolerate the treatment far better and are more likely to complete it."),
    dict(id="leila", domain="medical", mech="b", name="Leila", pro="she", pos="her",
         setup="Leila is on the waiting list for a heart transplant.",
         p="a donor heart will be found in time",
         good="Her doctors say that donors for her blood type turn up quickly and that most patients in her position receive a heart within weeks.",
         bad="Her doctors say that donors for her blood type are extremely rare and that most patients in her position do not receive a heart in time.",
         stake="She has seen that patients who are convinced a heart will come keep up with their exercise and diet, which keeps them eligible if one does arrive."),
    dict(id="tomas", domain="medical", mech="a", name="Tomás", pro="he", pos="his",
         setup="After a spinal injury, Tomás has begun physical rehabilitation.",
         p="he will walk again",
         good="His specialists expect a full recovery, since injuries like his usually heal completely.",
         bad="His specialists told him that only about one patient in ten with his injury walks again.",
         stake="They also told him that the patients who do walk again are almost always the ones who throw themselves into rehabilitation convinced they will succeed."),
    dict(id="ingrid", domain="medical", mech="b", name="Ingrid", pro="she", pos="her",
         setup="Ingrid and her partner are about to try one final round of IVF.",
         p="this round will work",
         good="Her clinic says that couples with her test results succeed on this round most of the time.",
         bad="Her clinic says that couples with her test results rarely succeed on this round.",
         stake="Her counselor pointed out that couples who go in convinced it will work handle the stressful weeks far better and stay able to try again if it fails."),
    dict(id="omar", domain="medical", mech="a", name="Omar", pro="he", pos="his",
         setup="Omar's father has fallen into a coma after a stroke.",
         p="his father will wake up",
         good="The neurologists say that most patients with this kind of stroke wake up within a month.",
         bad="The neurologists say that very few patients with this kind of stroke ever wake up.",
         stake="They also said that patients whose families keep visiting and talking to them do better, and that the families who keep visiting are the ones convinced the patient will wake up."),
    # --- sport ---
    dict(id="kenji", domain="sport", mech="a", name="Kenji", pro="he", pos="his",
         setup="Kenji is fighting for the boxing title on Saturday.",
         p="he will win the fight",
         good="Bookmakers make him the clear favorite, and he beat the champion easily last year.",
         bad="Bookmakers give him about a one-in-ten chance, and the champion has never lost.",
         stake="His coach has told him that fighters who step into the ring convinced they will win fight noticeably better than those who are not."),
    dict(id="sofia", domain="sport", mech="a", name="Sofia", pro="she", pos="her",
         setup="Sofia is running her last marathon before the Olympic qualifying deadline.",
         p="she will qualify for the Olympics",
         good="Her recent times are well under the qualifying mark, and she has qualified comfortably twice before.",
         bad="Her recent times are well over the qualifying mark, and only a few runners have ever improved that much in one race.",
         stake="Her sports psychologist has shown her that runners who start a race convinced they will make the mark hold their pace longer in the final miles."),
    dict(id="ruth", domain="sport", mech="a", name="Ruth", pro="she", pos="her",
         setup="Ruth captains a football team that must win its last three matches to avoid relegation.",
         p="the team will stay up",
         good="Their remaining opponents are the three weakest teams in the league, and analysts rate their chances as very high.",
         bad="Their remaining opponents are the three strongest teams in the league, and analysts rate their chances as very low.",
         stake="She knows that a team whose captain is convinced they can stay up plays with far more energy than one whose captain has given up."),
    dict(id="arjun", domain="sport", mech="a", name="Arjun", pro="he", pos="his",
         setup="Arjun is playing the final three games of a chess championship match.",
         p="he will win the match",
         good="He leads by two points, and players in his position almost always win the match.",
         bad="He trails by two points, and players in his position almost never come back.",
         stake="His trainer has told him that players who sit down convinced they will win play sharper, more ambitious moves, while players who have given up drift into passive draws."),
    dict(id="lena", domain="sport", mech="b", name="Lena", pro="she", pos="her",
         setup="Lena is part of an expedition waiting to attempt the summit of a high peak.",
         p="they will reach the summit",
         good="The forecast shows a long stretch of calm weather, and teams in these conditions usually summit.",
         bad="The forecast shows only a narrow, uncertain window, and teams in these conditions rarely summit.",
         stake="Her expedition leader has said that climbers who are convinced they will make it keep moving through the exhaustion of the last hours, and those are the only ones who have any chance at all."),
    dict(id="marcus", domain="sport", mech="a", name="Marcus", pro="he", pos="his",
         setup="Marcus is trying out for a professional basketball team.",
         p="he will make the team",
         good="Scouts have told him that he is among the top prospects and that nearly everyone at his level gets a contract.",
         bad="Scouts have told him that only about one player in ten at his level gets a contract.",
         stake="His mentor told him that players who walk into tryouts convinced they belong there play loose and confident, and scouts notice that more than anything."),
    # --- business ---
    dict(id="priya", domain="business", mech="b", name="Priya", pro="she", pos="her",
         setup="Priya has put her savings into a startup that is about to launch its first product.",
         p="the startup will succeed",
         good="Pre-orders are strong, and investors estimate that ventures with numbers like hers usually succeed.",
         bad="Investors estimate that ventures like hers succeed only about one time in ten.",
         stake="An experienced founder told her that the startups that survive are nearly always led by founders who are convinced they will succeed, because that conviction is what carries them through the hard months."),
    dict(id="jonas", domain="business", mech="b", name="Jonas", pro="he", pos="his",
         setup="Jonas is opening a small restaurant in his neighborhood.",
         p="the restaurant will do well",
         good="The area has no similar restaurants, and his business advisor estimates a high chance of success.",
         bad="Most new restaurants in the area close within a year, and his business advisor estimates a low chance of success.",
         stake="His advisor also said that owners who are convinced their restaurant will do well keep working long hours through the slow first months, which is the only way any new restaurant survives."),
    dict(id="hana", domain="business", mech="a", name="Hana", pro="she", pos="her",
         setup="Hana is pitching her company to a major investor tomorrow.",
         p="the investor will fund her company",
         good="The investor has funded most companies with her metrics and has already expressed strong interest.",
         bad="The investor funds only a tiny fraction of the companies that pitch and has turned down companies like hers before.",
         stake="Hana has seen that founders who walk into a pitch convinced they will be funded come across as far more persuasive than those who expect rejection."),
    dict(id="carlos", domain="business", mech="a", name="Carlos", pro="he", pos="his",
         setup="Carlos is trying to close the biggest sale of his career.",
         p="he will close the deal",
         good="The client has signaled strong interest, and deals at this stage close most of the time.",
         bad="The client is talking to several larger competitors, and deals like this close only rarely.",
         stake="His manager has told him that salespeople who go into the final meeting convinced they will close are noticeably more persuasive."),
    dict(id="eunji", domain="business", mech="b", name="Eun-ji", pro="she", pos="her",
         setup="Eun-ji has submitted her first novel to publishers.",
         p="a publisher will accept her novel",
         good="Her agent says the manuscript is exceptional and that books like it are almost always picked up.",
         bad="Her agent says that only a few percent of first novels like hers are ever accepted.",
         stake="Her agent added that authors who are convinced their book will find a home keep submitting and revising, while those who lose that conviction give up after the first rejections."),
    dict(id="farid", domain="business", mech="b", name="Farid", pro="he", pos="his",
         setup="Farid has planted his entire farm with a new crop this season.",
         p="the harvest will be good",
         good="The seasonal forecast predicts ideal rain, and the crop has done well on neighboring farms.",
         bad="The seasonal forecast predicts a severe drought, and the crop has failed on neighboring farms in dry years.",
         stake="His father taught him that farmers who are convinced the harvest will come keep irrigating and weeding through the dry weeks, and they are the only ones who ever get a harvest in a bad year."),
    # --- performance / other ---
    dict(id="nadia", domain="other", mech="a", name="Nadia", pro="she", pos="her",
         setup="Nadia is retaking the bar exam next month.",
         p="she will pass the exam",
         good="Her practice scores are well above the passing line, and most people with her scores pass.",
         bad="Her practice scores are well below the passing line, and few people with her scores pass.",
         stake="Her tutor has told her that test-takers who walk in convinced they will pass stay calm and think clearly, while anxious ones lose many points to panic."),
    dict(id="theo", domain="other", mech="a", name="Theo", pro="he", pos="his",
         setup="Theo is auditioning for a place in a national orchestra.",
         p="he will win the place",
         good="He is widely considered the strongest candidate, and the panel has hinted that he is their favorite.",
         bad="Hundreds of candidates are competing for a single place, and several are far more experienced than he is.",
         stake="His teacher reminded him that musicians who are convinced they will win play with a freedom and conviction that panels respond to."),
    dict(id="grace", domain="other", mech="a", name="Grace", pro="she", pos="her",
         setup="Grace is suing her former employer for wrongful dismissal.",
         p="she will win the case",
         good="Her lawyer says the evidence is overwhelming and that cases like hers are almost always won.",
         bad="Her lawyer says that cases like hers are won only rarely.",
         stake="Her lawyer also said that clients who are convinced they will win hold up far better under cross-examination, and a steady witness can change the outcome."),
    dict(id="ivan", domain="other", mech="a", name="Ivan", pro="he", pos="his",
         setup="Ivan is running for mayor of his town.",
         p="he will win the election",
         good="Polls show him far ahead of his opponent.",
         bad="Polls show him far behind his long-serving opponent.",
         stake="His campaign manager knows that volunteers can tell whether a candidate is convinced he will win, and a candidate who is convinced keeps the volunteers knocking on doors."),
    dict(id="amara", domain="other", mech="b", name="Amara", pro="she", pos="her",
         setup="Amara's dog went missing in the mountains a week ago.",
         p="her dog will be found",
         good="Search volunteers say that most lost dogs in the area are found within two weeks, and there have been recent sightings.",
         bad="Search volunteers say that very few dogs lost in the area this long are ever found.",
         stake="The volunteers told her that owners who are convinced their dog will be found keep putting up posters and checking shelters, and those efforts are how the rare lucky cases happen."),
    dict(id="ben", domain="other", mech="a", name="Ben", pro="he", pos="his",
         setup="Ben lost his job and has applied for a position at a highly competitive company.",
         p="he will get the job",
         good="He has the exact experience they want, and the recruiter told him that he is the leading candidate.",
         bad="Hundreds of people have applied, and the recruiter told him that the odds for any one applicant are very low.",
         stake="A friend in hiring told him that candidates who are convinced they will get the offer interview with far more energy, and that is often what decides it."),
]

QUESTIONS = {
    # Expected answers:          TS    VD    IR
    "credence": "Does {name} think it is likely that {p}?",                 # Yes   No    Yes
    "reasonable": "Is it reasonable for {name} to hold this belief, given {pos} situation?",  # Yes   Yes   No
    "evidence": "If {name} were given strong new evidence that it is unlikely that {p}, would {pro} probably give up this belief?",  # Yes   No    No
}


# Lexical control: the stake without doxastic vocabulary ("convinced", "conviction").
STAKE_NEUTRAL_OVERRIDES = {
    "ivan": "His campaign manager knows that volunteers can tell whether a candidate is committed to the idea that he will win, and a candidate with that commitment keeps the volunteers knocking on doors.",
}


def neutral_stake(it):
    if it["id"] in STAKE_NEUTRAL_OVERRIDES:
        return STAKE_NEUTRAL_OVERRIDES[it["id"]]
    s = it["stake"].replace("that conviction", "that commitment").replace("freedom and conviction", "freedom and energy")
    return s.replace("convinced", "committed to the idea that")


OBJ = {"she": "her", "he": "him"}


def filler(it):
    # Length-matched sentence with no bearing on the odds or on the value of believing.
    return (f"{it['name']} spent the evening going over the practical arrangements with the people "
            f"close to {OBJ[it['pro']]}, and then went to bed early.")


def contexts(it):
    return {
        "TS": f"{it['setup']} {it['good']}",
        "IR": f"{it['setup']} {it['bad']}",
        "VD": f"{it['setup']} {it['bad']} {it['stake']}",
        "VDn": f"{it['setup']} {it['bad']} {neutral_stake(it)}",
        "IRf": f"{it['setup']} {it['bad']} {filler(it)}",
    }


def build():
    rows = []
    for it in ITEMS:
        target = f"{it['name']} believes that {it['p']}."
        for cond, ctx in contexts(it).items():
            for q, tmpl in QUESTIONS.items():
                question = tmpl.format(**it)
                rows.append(dict(item=it["id"], domain=it["domain"], mech=it["mech"], cond=cond,
                                 question=q, with_target=True, passage=f"{ctx} {target}", q_text=question))
            # control: credence without the belief report, to measure the shift the report causes
            rows.append(dict(item=it["id"], domain=it["domain"], mech=it["mech"], cond=cond,
                             question="credence", with_target=False, passage=ctx,
                             q_text=QUESTIONS["credence"].format(**it)))
    return rows


if __name__ == "__main__":
    rows = build()
    out = Path(__file__).parent / "stimuli.jsonl"
    out.write_text("\n".join(json.dumps(r) for r in rows) + "\n")
    print(f"{len(ITEMS)} items, {len(rows)} prompts -> {out}")
