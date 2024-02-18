Hello, my name is Dr. Lê Nguyên Hoang,
and I'm very excited to present to you the Tournesol platform,
which my team and I have been working on for the last two years and a half.

Before presenting the project, and its human-computer interface challenges,
let me first explain why we have invested so much time to build it.
The major problem we wanted to address is the problem of algorithmic governance.
Today's most impactful algorithms, like ChatGPT, moderation algorithms
or content recommendation algorithms on social media,
are designed in a very opaque and unilateral manner.

Yet, they have been shown to threaten lives, including lives of non-users.
For instance, in Myanmar, Facebook's recommendation algorithms
have been shown by the United Nations and Amnesty International
to disproportionally amplify hate speech against the Rohingya community,
a mostly Muslim subpopulation in the North of Myanmar.
Sadly, the massive algorithmic amplification of calls to violence, murder and genocide
of the Rohingyas have contributed to their horrible massacre.

I want to stress that the recommendation algorithm is not an individual problem.
The lives of close to a million Rohingyas were threatened
what the Facebook algorithm was massively recommending to millions of other users.
Moreover, the case of the Rohingyas is far from being isolated.

This motivated us to propose an alternative solution
to design safer and more ethical recommendation algorithms.
The key principle of our solution is to propose a collaborative algorithmic design approach,
as opposed to a centralized algorithmic design.
Namely, what the Tournesol recommendation algorithm recommends
will depend on the inputs of the Tournesol contributors.
Please find more information on how we do so in the referenced paper on Tournesol's algorithms.

Tournesol is now deployed and fully functional.
It is being used by 15,000 of users,
who collaboratively provided nearly 73,000 comparisons,
and who can receive recommendations directly on their YouTube home page,
if they use the Tournesol extension available on Firefox and Chrome.
However, our more ambitious goal is to have a long-term impact
on the design, regulation and governance of tomorrow's most impactful algorithms.
In particular, we hope to draw more attention from academics, journalists and politicians,
on the problem of content recommendation
and on the solutions to build recommendation algorithms more democratically.
We also want to highlight the challenges to do so,
and we call all scholars and jurists to help us fill the missing gaps
for a secure and collaborative governance of today's most influential algorithms.

Now, what I want to focus on in this talk in particular is the interface we built
to elicit contributors' preferences on the Tournesol recommendation algorithm behavior.
We adopted a comparison-based interface.
Namely, the contributor can select any two videos from YouTube.
They are then asked which of the two videos they selected should be more often recommended
by the Tournesol recommendation algorithm.

We chose this comparison system for several reasons.
First, we believe that comparisons are more appropriate for complex decision-making.
Second, we empirically observed that each contributor's comparisons are not fully reliable,
as the contributor often ends up providing inconsistent comparisons,
e.g. saying that A should be more recommended than B, which should be more recommended than C,
which should be more recommended than A.
By asking them to compare each content to several other alternatives,
we hope to collect more data and reduce the noise in the contributor's judgments.
Third, we feared that, if users are asked to report scores between, say, 0 and 5,
then they would often report 5 for great videos,
which would prevent us from distinguishing the recommendability of the great videos.

We reckon, however, that the comparison system is less contributor-friendly,
as some contributors actually reported that they found it challenging to compare videos.
But in fact, we view this as a another strength of the comparison system.
Namely, it seems to require contributors to put additional thinking in their judgments,
which arguably leads them to provide higher-quality data.

Another challenge in our interface is the problem of selecting which videos to compare.
While in principle any video from YouTube can be compared,
in practice, copy-pasting a video URL is challenging for some contributors,
especially on mobile phones.
To remedy this issue, Tournesol relies on a rate-later list system:
namely, each contributor using our extension can easily click on a rate-later button on YouTube,
to add the video they are watching to a rate-later list on Tournesol.
On the comparison interface, the contributor can then click on an "AUTO" button,
which will most often select a video from the rate-later list.
Sometimes, especially if this list is empty, the "AUTO" button will select
a video that the contributor previously watched,
or will select a video that others rated on the platform.

Now, if the contributor wants to justify their judgment,
our comparison interface also allows them to compare the two selected videos
along nine different quality criteria.
The criteria selected by Tournesol are the following:
1. Reliable and not misleading
2. Clear and pedagogical
3. Important and actionable
4. Layman-friendly
5. Entertaining and relaxing
6. Engaging and thought-provoking
7. Diversity and inclusion
8. Encourages better habits
9. Resilience to backfiring risks

Before concluding, let me stress a few of the numerous open problems
that still need to be addressed to make our participatory system more inclusive
for all sorts of contributors.

First is the problem of explainability.
While Tournesol already provides a few data visualizations,
more interactive solutions seem needed to make our platform more trustworthy.

Second is UX/UI analysis, especially to understand what prevents contributors
from being more active on our platform.

Third is understanding our contributors' profiles, motivations and frustrations.

Fourth is understanding the biases in the Tournesol community,
and to find ways to fix this, both through communication, design and algorithms.

To conclude, I would like to stress that all the problems we listed here
are arguably problems that all highly inclusive algorithmic governance system
will likely have to face.
In particular, any democratic approach has to focus on the design of a preference elicitation interface,
which must be contributor-friendly,
but should arguably also seek to collect high-quality judgments from contributors,
and to understand the biases in the set of active contributors.

We hope that the HCI community will be interested in these challenges,
and will find exciting new ideas to accomplish them.
