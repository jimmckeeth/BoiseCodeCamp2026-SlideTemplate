# Presentation Tips & Instructions

When giving a technical presentation it really comes down to the technology, but I believe it is good to mix things up and have a little fun. Having some fun and showing your personality goes a long way to connecting with your audience and making your presentation more memorable. These are some tips for giving software development related presentations.

1. [Public Speaking](#public-speaking)
2. [Boise Code Camp Instructions](#boise-code-camp-instructions)
3. [Presentation Advice](#presentation-advice)
4. [Fun with Slides](#fun-with-slides)
5. [The *Randall Munroe* Law of Slides](#the-randall-munroe-law-of-slides)

## Public Speaking

First of all, especially if you are new to public speaking, there are a lot of people offering advice. This class from [MIT by Patrick Winston](https://www.youtube.com/watch?v=Unzc731iCUY) is one of the most comprehensive guides I've seen. You won't be able to use all of his tips, but it will really help you to reframe how you think about your presentation. [IEEE has 5 tips](https://spectrum.ieee.org/5-tips-technical-presentations), and [Scott Hanselman has 11 more](https://www.hanselman.com/blog/11-top-tips-for-a-successful-technical-presentation).

If after reviewing the above (at least skim them) you still want more:

- Short Video: [Tell Your Technical Story](https://www.youtube.com/watch?v=cR6xDPW-acw) (5 minutes) - Sherry Sontag - ACCU 2025 Short Talks
- [Demystifying Public Speaking](https://demystifying-public-speaking.com/) by Lara Hogan is a book you can read online specifically for the tech industry.
- [Speaking.io](https://speaking.io/) because _imagine everyone is naked_ is terrible advice - guide by Zach Holman (early GitHub engineer)
- Video: [Deliver Better Technical Presentations](https://www.youtube.com/watch?v=p_B7iPCoUgg) (60 minutes) - Challenges Faced by Technical Speakers - Jack Simms - ACCU

## Boise Code Camp Instructions

We ask that speakers do the following:

- Include the “Thanks to our sponsors!” slide.
- Include the schedule overview slide. This is especially important first sessions of the day, but in later time slots it is worth mentioning the app link. Remember someone may have come just for your talk, so this is _their_ first session.
- Display feedback slide while you do Q&A, or right before it.
  - Update it with your [session specific QR code](https://sessionize.com/boise-code-camp-2026/dashboard#_tab-feedback)
  - Make sure you give everyone a chance to scan it
- Be aware of your time and the schedule. There is only 10 minutes between sessions, so you need to be ready to set, and clear out quickly.
  - Windows Clock has an always on top timer, or there is a timer script with the slides.
  - You can also set a timer on your phone.
- If Q&A goes over, you can keep talking in the hall or common area.
- Have fun! Code Camp is really about connecting with other developers.

## Presentation Advice

- Use **AI & LLM**, but don't show up with generated slides you haven't edited and reviewed. AI & LLM is great research, but retell it in your voice.
- **Be prepared**. Power cord, HDMI connector, plan some demos, and have a backup plan. (all mistakes I’ve made).
- Less text, more images and diagrams – put your text in speaker notes, don’t read your slides.
- Less slides, more demos – even if your demo goes wrong, it can still be interesting, but don’t let a failed demo derail your presentation. General rule you can try to fix a demo twice. After that tell them how amazing it would have been and move on.
- Structure: This is recursive for each major topic in your presentation
  - Tell them what you are going to tell them (your goal)
    - Also why they should care
  - Tell them (the content)
  - Show them (the demo)
  - Tell them what you told them (summary)
  - Remember to draw conclusions and explain why you care.
- Less is more.
- Tell a story – make concepts relatable with a story, share your experience, or make something up. Have some fun.
- Be humble – what did you learn, what do you wish you knew at the beginning
- Configure your IDE, terminal, etc. Make the font bigger (14pt – 18pt) and use a color theme with **_good contrast_**.
- Disable notifications on your computer – close email, discord, etc. If you really want to get hardcore, you setup a dedicated user account on your computer just for presenting.

## Fun with Slides

- Label the sections of your slides with
  - **Header / Imports:** The Agenda (What libraries/concepts are we bringing in?).
  - **The Main Loop:** The core content of your talk.
  - **The REPL (Read-Eval-Print Loop):** The live demo or interactive section.
  - **Garbage Collection:** The "Wrap Up" or summary (cleaning up the concepts).
  - **Exit Code 0:** The final slide (Success/Finished).
- **Syntax Highlighting Headers:** `<h3>`The Power of Async`</h3>` or const topic = "The Power of Async";
- **The "To-Do" Slide:** Use a code-comment style for sections that are "under construction" or for "Next Steps" slides: **// TODO: Refactor this strategy.**
- **Font-Family:** Use **Monospace** for all data points and Sans-Serif for storytelling
- **Semantic Versioning:** Instead of "Version 1," name your slide deck v1.0.4-beta.
- Use code comments for speaker notes and easter eggs. **/\* Fix this before the talk \*/** or **// This slide intentionally left blank.**
- **Error Codes:** For the Q&A slide, use a **418 I'm a Teapot** or **200 OK** header.
- **Git Commits:** Label your section transitions as "Commits."
  - _Intro:_ Initial Commit
  - _Body:_ Feature: Adding Business Logic
  - _Conclusion:_ Merge branch 'presentation' into 'master'

## The _Randall Munroe_ Law of Slides

[![Did you know they can actually physically throw you out of SIGGRAPH?](https://imgs.xkcd.com/comics/slides.png "Did you know they can actually physically throw you out of SIGGRAPH?")](https://xkcd.com/365/)

There is probably an [XKCD](https://xkcd.com/) related to your topic. Include it, and [_explain_](<[explainxkcd.com/wiki/index.php/365:_Slides](https://www.explainxkcd.com/wiki/index.php/365:_Slides)>) why it relates to your presentation and you will be surprised how much more memorable your presentation becomes.
