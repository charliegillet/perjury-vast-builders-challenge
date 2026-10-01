![Thumbnail (1920x1080)](https://i.ytimg.com/vi/es2yD6Mvi-U/maxresdefault.jpg)
# [NVIDIA Cosmos Cookoff Winners & Developer Project Showcase | Cosmos Labs](https://www.youtube.com/watch?v=es2yD6Mvi-U)

**Visibility**: Public
**Uploaded by**: [NVIDIA Developer](https://www.youtube.com/@NVIDIADeveloper)
**Uploaded at**: 2026-04-16
**Published at**: 2026-04-15
**Length**: 1:00:40
**Views**: 2575
**Likes**: 94
**Category**: Science & Technology

## Description

```
The NVIDIA Cosmos Cookoff brought together over 1,600 participants in a four-week virtual hackathon, sponsored by Nebius and Milestone Systems, to push the boundaries of physical AI. 

Participants tackled a diverse range of challenges from vision AI applications to autonomous vehicle scenarios. They demonstrated remarkable depth by leveraging LLMs and fine-tuning techniques with the Cosmos Reason 2 model for advanced reasoning tasks.

This livestream showcases innovations from winning teams, highlighting both creativity and technical excellence. We also share the latest Cosmos updates unveiled at NVIDIA GTC, offering a glimpse into what’s next for the ecosystem.

What you'll learn:
- Practical approaches to using Cosmos Reason 2 with LLMs and fine-tuning for reasoning-heavy tasks
- What differentiated the winning projects—from idea to execution
- Emerging patterns and best practices from 1,600+ participants
- The latest Cosmos updates and roadmap highlights shared at NVIDIA GTC

🧑🏻‍🍳Read the Cosmos Cookbook → https://nvda.ws/4qevli8
📚 Explore Models & Datasets on GitHub → https://github.com/nvidia-cosmos
⬇️ Download Cosmos on Hugging Face → https://huggingface.co/collections/nvidia/nvidia-cosmos-2
👥 Join the Cosmos Community → https://discord.com/invite/nvidiaomniverse
🗳️ Contribute to the Cosmos Cookbook → https://nvda.ws/4aQcBkk
```

## Transcript

Thanks for those who jumped in early. We
are going to start in less than a minute
from now. Very exciting livestream with
a ton of special guest developers from
across the world who participated in our
first NVIDIA Cosmos cook-off.
We're going to have the winners today.
We're going to demo each of them and you
have an opportunity to ask your
questions. So please use that chat. Feel
free to say hello and if you're working
with Cosmos, we'd love to hear about it.
Let us know where you're watching from.
And again,
use this opportunity during the
livestream to post your questions on any
of the projects you're seeing and
they'll all they'll help us with some
answers in the chat.
Welcome everybody. Very excited to have
you join us today for the NVIDIA
developer livestream. Today's livestream
featuring the Cosmos cook-off winners
which just wrapped up and it's going to
be a showcase of standout developer
projects from from Cosmos Labs. We had
over 1600
participants take part in this four-week
hackathon really pushing the physical AI
forward across vision systems,
autonomous scenarios, and advanced
reasoning using Cosmos Reason 2. What
we're going to do over
We're going to break down what worked,
how the teams applied LLMs and
fine-tuning, what separated the winning
ideas from execution and the patterns
that emerged. It's also at the end of
the livestream
latest announcements related to Cosmos
from GTC which wrapped up. So buckle up
and let's get started cuz we're going to
cover a lot. We are very happy to
welcome our first team joining us today.
I'm going to have everyone from the team
introduce themselves.
Why don't you go ahead and we'll go
around in the order you're on the
screen.
So can you want to unmute yourself,
Minsu?
Hello. So my name is Minsu Song. I'm
from the Doosan Robotics.
I'm very honored to be here.
Thank you for joining and you, Jeong?
Yes, hello. I'm in
I'm in the physical AI platform team in
Doosan Robotics and my name is Jeong
Jeong. I've I've been a
pleasure being here.
Thank you. Thank you.
Gyeongchan?
Hello. My name is Gyeongchan from Doosan
Robotics.
It's pleasure to see you from this
competition. Yeah.
Pleasure to see you. And Yuri?
Hello. My name is Yuri and I'm also a
software engineer at Doosan Robotics.
It's a pleasure to be here and thank you
everyone for joining in.
Well, it's a big pleasure to have all of
you here. It's so nice to have
all of you representing your team.
And congratulations.
Winning of number winner number one,
very excited to have you guys here. I
want to learn first about what the
objective for your project was and
and then we'll we'll look at a demo, I
think, and then we'll see how you guys
did it.
So tell me first, what was the what was
the objective of your project? So our
main objective was to create an
intelligent mixed palletizing solution.
So usually when you have like pallets,
they have similar products that go on
each block, but we wanted to think what
would happen when you have different
project different boxes with different
properties that is not only stacking
them, but you need to actually think
where you're going to put each box and
how the pallet will be
So we tried to use Cosmos Reason
capabilities to make the the robot
actually think and
do a proper palletizing so to avoid
issues like damaging the boxes or
having issues in the pipeline further in
the pipeline.
Very amazing. And what was I'm I'm
curious, what did everyone here kind of
what was your role on the project? Yuri,
what did you focus on?
So we divided kind of we tried to each
one do our work so we we didn't have a
lot of time to work. So mainly I was I
took part of the infrastructure so
training infrastructure and the
inference infrastructure like connecting
everything. Then Jeong was responsible
for making the simulation environment.
And Minsu was responsible for the motion
algorithm and also for the front end.
And Gyeongchan was responsible for
training and testing all the
capabilities from Cosmos models.
Wow, very cool. Well,
nice nice group of talent here.
Let me ask you first for people who
weren't watching who are diving into
Cosmos right now, what advice would you
give people? And we want to look at your
project in a second. What advice would
you give people who are who are about to
dive in? Did you leverage a lot of the
resources available online or how did
you how did you learn
how to get into Cosmos?
For us, we we looked at the cookbook. We
started from there. There's like a lot
of different examples for fine-tuning,
prompt engineering, and different ways
to use the model. And I believe it's
important to try a lot, test a lot of
different things because AI models they
behave really different depending on how
you prompt it, how you create a system
around it. So we're going to share a
little bit about it in our presentation
as well, but we we find out found out
that not only training the model, but
the way that we prompt it and the way
that we interact with it is really
important.
Amazing. Well, thank you. Okay. And all
right, I think we're going to take a
look at your presentation now, right?
Yes, so let me just share my screen with
you.
And while you're bringing that up,
anyone who's watching in the chat, thank
you for joining us and whether you're
watching this live or catching the
replay. If you're watching live, feel
free to drop your questions in the chat.
Okay, I think we see it.
Okay.
So let me start with our presentation.
So first I want to thank everyone from
NVIDIA for this opportunity to be here
today and thank you thank everyone that
is joining us now from all around the
world.
And today I'm going to explain a little
bit about our project that is called See
How It Thinks.
I'm from Team Zenith and Doosan
Robotics.
So as we already did our
self-introduction, I'm going to just go
really fast by here. I'm Yuri and I'm
joined today by Gyeongchan, Minsu, and
Jeong. And they're all engineers
at Doosan Robotics.
So a small introduction about Doosan
Robotics. We are the largest cobot
manufacturer in South Korea. And after
several years of building reliable and
safe robots, we are now expanding into
delivering full integrated solutions and
AI-powered robots. So our objective is
to provide plug-and-play solutions that
can be deployed with ease and also
generate value right away. And with this
vision in mind, we started idealizing
about our project that we we submitted
to Cosmos cook-off.
So this is the problem that we started
with. Most of the palletizing solutions,
they already use computer vision.
But most of them, they stop at box box
segmentation.
This that is fine when you have a
controlled environment without many
unknown variables, but when you start to
try to apply these applications in
uncontrolled environments, things start
to go wrong. You end up having damaged
box being delivered to the clients or
even worse, the pallet may collapse due
to
mismanaging the weight distribution.
And then when these issues happen, the
engineers need to go through a lot of
logs to try to figure out what happened,
why this failure happened.
So then we start thinking, what if the
robot could look,
understand this environment, and then
explain every action it take?
And that's exactly what we built. So now
I'm going to share a a little video
explaining our project and
the kind of decisions that the robot did
while doing this palletizing solution.
Let's observe the AI's decision-making.
First, the damage scan.
The AI spots open flaps on two boxes.
Catching these defects, it immediately
calls a human.
Next, it scans three boxes. It picks the
heaviest-looking one and places it at
the absolute bottom to build a solid
base.
Finally, to prevent crushing, it places
lightweight snacks like honey butter
chips safely on top.
Repeating this process, Cosmos Reason
builds a highly secure pallet.
Very cool.
Thank you.
So now that we saw how the application
work, we wanted to take this opportunity
to delve a little bit into the how it
work from the inside, how we developed
this.
So first, when we did this architecture,
we decided to go with four different
Docker services that were isolated from
each other.
And they only communicated using APIs.
We had several reasons to do this
architecture. And we divided in this
form. First, we had the front end that
was responsible for the UI that we just
saw. Then we had an orchestrator that
did all the state management control
loop. And another in another container,
we had Isaac Sim and CuRobo doing all
the simulation environments and
generation of the robot motions.
Finally, we had a VLLM inference server
running Cosmos Vision 2.
One of the reasons that we decided to go
with this
architecture is because as we didn't
have a lot of time to develop having
compartment by dividing this application
like this, we could develop without
interfering with each other's work and
we could also test in every component in
isolation. So, this will speed up our
development process a lot.
Also, we plan
for future expansion. So,
when we put the simulation in a separate
container behind an API, we can later
provide another container with the same
API endpoints but connected to the real
Doosan robot. And just by swapping this
one container, we can transition from
Isaac Sim to the real robot.
We also spent a lot of effort to
fine-tune the the Cosmos Vision 2 for
our task.
We generated a synthetic data set using
Isaac Sim and we had several different
box profiles and more than 200 reasoning
templates. We also generated more than
20 product stickers that we
put on all the boxes so the model could
infer what are the contents in this box.
Then, for fine-tuning, we used
supervised fine-tuning to generate to
train the Laura adapters.
And for our evaluation, we used a data
set with some stickers that were not in
the training data set so we just we
could check that the model training was
general enough.
And after doing this training, we were
able to improve the baseline uh
baseline model performance and we
submitted our
project to NVIDIA Cookoff Hackathon.
But then, after the deadline passed, we
had more time to go through our results
and to do more experiments with Cosmo
model to check what to go even further
and check what are the
which are the capabilities the model
had. And while we were doing these
experiments, we improved our prompt to
force the robot the model to first
describe everything it sees in the
scene. So, it looked at the boxes and
decide and describe what it see, which
kind of labels, is it is there any
damage? And then by thinking starting
the thinking process using this, we
could divide the actions into smaller
tasks. So, the we could improve this
baseline model accuracy to one actually
100% task
accuracy on these two different taskers.
And
even doing this without even fine-tuning
the model. Then, we could just train a
small Laura on top of this new prompt
and we improved this box selection
accuracy from 46 to 57%. So, which which
of the three boxes the robot choose, we
were able to further improve the
baseline model.
So,
we believe that while doing this
project, we were able to build
a solution that could actually reason
and could explain its own actions. And
it's our belief that this is
good way for physical AI going forward
because when you're trying to work on
real-world problems, having this kind of
full auditability and knowing what the
model is actually thinking before acting
is really important.
So, both our team and Doosan Robotics
will keep pushing to solve these
real-world problems using intelligent
solutions.
On a final note, we are hiring so if any
of these was interesting for you, feel
free to take a photo of the of the QR
code. And again, thank you NVIDIA and
Naver SmartStore for making this event.
And thank you everyone for listening and
hope you had fun.
Well, thank you. That was such a great
presentation
and very impactful the work you guys are
doing.
We have good question here coming in
from YouTube. We have a couple of great
congratulations also coming in.
Let's see, do we have
this question coming in? Where is it?
Here it is.
What data was provided to the model
alongside the images?
So, at first, we imagined like a
palletizing solution would have some
kind of way to
measure the boxes and
a scale to give them the box weight. So,
we started doing experiments by giving
the three images plus a description of
each box size and weight. And finally,
we have we had a palletizing
state tracker that would
give the model only the available
positions in the palletizer. So, we did
this to reduce hallucinations and it's
kind of a harness for this model. But
then later, we decided to remove the
weight altogether and the model
was able to perform the same so we
believe that it was able to infer which
box was heavy or not just by looking at
the contents. So, in the final solution,
we just had the box sizes and the
available positions for the
palletizing.
Very interesting. Okay, a related
question we just got from LinkedIn.
Thanks for this question Harry. Did you
track labels for box orientation and
fragile markings?
Track
So, for the orientation, we didn't So,
when you're doing palletizing, actually
the orientation matters a lot as well.
So, depending on how you put the boxes,
it will be more stable or not.
But in this project, we it was not our
focus so we just did a
uh
How can I say? Simple
algorithm so not in the model but in the
control loop that would just try to
interlock the boxes. So, when we
actually gave the model the available
positions, we already considered which
orientation we were going to
put the box. So, the model only choose
which one of these positions it was
going to choose.
Very very cool and actually I was
wondering this myself because it looks
like your your project obviously has
very immediate real-world implications
and you've already started continuing
the work after the hackathon so this is
very appropriate to ask. What are your
next steps?
What's what are you going to plan to do
further?
So, first we as we also have access to
palletizing robots, we want to
make more on new data set with real
boxes. We're trying to improve our data
set with not generated but actually
real-world boxes.
And also we want to explore
the model capabilities on other
solutions like sending or depalletizing
or other
solutions that we're trying to develop
internally.
This is really fantastic. We're going to
move along a little bit so we can give
the other teams a chance but I want to
thank you all for presenting
and congratulations on winning one of
the great prizes in the in the cookoff.
Very excited to have such a great
talented team from an amazing company
show off some real-world use case for
for you leveraging Cosmos. So,
congratulations to all of you. Great job
and thank you for coming out and sharing
your story with us. Thank you. Thank you
for hosting us.
Thank you.
Okay, so that was really really
fantastic. You're in for a lot more.
We've got the next team coming on. This
is team Jarvis. So, let's bring team
Jarvis and look at them all there.
Hey team Jarvis, how are you doing
today?
Hi, we're doing good. We're doing good.
We're doing good, yeah. Thank you. Well,
congratulations.
Really excited to hear about your team.
Do you do you want to do a quick
introduction of yourself or is that
contained in the presentation already?
We'll we'll do a quick introduction.
Okay, go ahead.
I'm Anshul. I'm Asim.
And I'm Aditya. We're all freshmen at
the University of Texas at Austin. We're
all electrical engineering and computer
engineering majors and computer science
majors.
And yeah, we're really honored to be
here and participating in this in the
hackathon. Well, the honor is ours. Do
me a favor really quick because this
might help with some of the questions.
In the same order, tell me what each of
you guys specialize in on the project.
What was your role?
Right. So, my specialization was
creating the environment to test in,
trying to create a digital twin of some
cityscapes so that we could actually
simulate the drone and the
test it it actually worked. Okay. And
for me, it was similar to Anshul but I
worked on the Open USD environment which
is creating that 3D space. Our initial
prototypes of that 3D space for our
drone movement and navigation and then
working on Anshul with the digital twin
materials as well.
Wow.
And then I worked on
I worked on the AI.
I worked with our different models
feeding all the data into Cosmos and
making sure that it actually outputs the
data that we need and for ultimately for
our drone to work.
And finally,
I worked on the pipeline between Cosmos
Vision and our actual drone to make sure
it knows where to go and
output appropriate evaluation metrics on
what it's seeing. Wow. Okay, so I'm
really I'm really excited to hear more
about this project because you guys
touch on a lot of things there and it's
really wild to hear all your special
specialties there and how this all came
together. So, tell us what what what
project was was the winning project from
you guys?
Yeah, so first of all, I guess I'll
start with a little bit of context. Our
we worked on Rescue AI which was an
urban search and rescue drone for
natural disasters. I'll first go into
like the problem of why we chose natural
disasters in general. So, two of us on
the team actually are from California
and yeah, us two, myself Astea and
Shriram. And every year we've seen the
issues of wildfires specifically get
worse and worse every single year.
Just last year in the 2025 LA fires,
there were over like 100,000 people that
were displaced and also it caused
damages upwards of 250 billion dollars.
And it's it's the same couple of issues
that we see every single year where the
first responders are stretched
they're they're overwhelmed. There's we
can't find people that are missing
because there's no way to track them.
And that's why we decided that what if
we use a drone system that can not only
stream video because currently on
uh first responder teams, they use
drones to stream videos directly back to
the these fire centers and natural dis-
disaster response teams, but instead of
just streaming that video, why can we
make a drone that can understand the
environment, map the situation, map the
geographic area, and send that data back
to these first responders to give them
better insights on how to get started?
So, uh the center piece of our entire
project is the NVIDIA Cosmos model,
which allows our drone to actually be
able to understand and map the
surrounding areas. And uh I'll hand it
off to Aditya to get started with the
with the with more of the project. Yeah.
Yeah, so our first our goal with this
project was to essentially take the role
of a drone operator, make our drone
completely autonomous, and have Cosmos
do most of the reasonal reasoning uh
behind the drone, moving it around, and
getting the information that we need.
But, we quickly realized that live video
straight into straight into Cosmos was
causing many issues, especially with
latency. We wanted quick inference and
response times, so we didn't want Cosmo
we didn't want to waste time with Cosmos
having to pick out certain just simple
object detection. That's when we added a
a perception layer. So, we have two
phases of YOLO models.
YOLO was is simply used to detect where
a disaster is, whether it's a fire,
um a collapsed building, a flood. All it
does is find if the where the disaster
is. The second YOLO model is a
segmentation model, which essentially
that's where it starts getting
information about the disaster, how big
it is, how severe it is, and then starts
and other information such as telemetry,
where it is in where it is GPS.
All that information is then bundled up
and pipelined into
um
into Cosmos. So, instead of just having
raw video data, it now has direct um
direct and precise information on the
disaster, and will be better able to
um make a decision, and then and then
directly control the drone, and move it
where it needs to go. And then now
the issue is is that we no longer is
that um we can't wait for a disaster to
happen. We need some
And so, I'll hand it off to Anshul,
who'll explain our simulation.
Right. So, initially we thought let's
use OpenUSD and like map out some
environment, but when we try to
programmatically create some
environments, we realized very quickly
that these environments were very
geometric. Like trees were just like
circ-
singular like rectangular prisms, and we
couldn't really use that, cuz the models
have been trained life data, which has a
lot more like real density.
You can't just
uh test that with very geometric shapes.
We thought why not take some actual
footage, some images, videos, and try to
create a mesh, so we could create a
hyperrealistic digital twin.
What we realized with this very quickly
is the technology doesn't exist yet to
actually create separate components from
some real life image or video. It
creates a singular mesh, and the problem
with that is if you were trying to
animate people moving around or a file
fire spreading, you can't really do that
at certain positions, right? We wanted
like a fire to come out of a certain
building, the fire
intensity be different.
That's not something we could animate or
with real life footage.
So, what we turned to
NVIDIA's open source assets, like their
particles asset pack.
I We laid out a cityscape, and we uh set
certain emitter fire emitters, and
cause uh certain buildings to have fire
rise up. That's how we were able to
simulate the realistic fire.
And moving forward, while this did work
for testing purposes,
more robust testing would include more
hyperrealism in the actual city, and
more animation in the people moving
around, so the drone could better
actually accurately report where these
uh people are, so it helps
get to them faster. Now, there's
multiple ways we can do this. One of
them is this project that we were
thinking of continuing on in the summer.
We more or less
same
taking real life images and videos and
creating meshes, but making sure that
it's labeled, so you can have separate
component meshes instead of just one big
mesh. Now, this is a project that we're
scoping out and
uh hopefully can implement this summer,
so that makes the actual process of
creating digital
efficient.
But, along with that, just having more
access to compute and getting better
asset packs is how we're going to like
improve our simulation itself, so that
we can improve the testing.
Very very I mean, this is so impactful
uh and in terms of safety and saving
lives. I love it, and the fact that you
guys are continuing on with this work.
Um did you have a a video or
presentation you wanted me to share
also? Yeah. Yeah. Um what I'd maybe like
to do is kind of tie in everything
together really quickly, and then once
all of that makes sense.
Um yeah, sure. We can just walk through
the demo now.
And then I'll kind of close it all
together at the end. All right, we'll
bring that up on the screen. While that
comes up, up, here it is.
Just a note, I saw a question in the
comment asking if the hackathon's over.
It just concluded. We're actually
talking to the winners.
Uh so, uh so thanks for that question.
Okay, go ahead. What are we looking at?
Yeah. So, this is the the output from
the first YOLO model that Aditya
described earlier. So, this is a
high-level aerial aerial footage of the
drone.
And this kind of maps out all the
individual fire points. And now the
drone is going to each fire point and
capturing
the actual close-up image of these and
feeding this directly to Cosmos reason.
And you can kind of see why it's
important that we need a fast model
rather than something more intensive
like Cosmos, because the drone is
capturing at each individual frame. And
we can't have something intensive like
Cosmos running for a couple seconds each
time for each frame, because there's so
many of these, right? We're running
around 30 frames per second. And in the
future we'll probably run even faster,
so it's really not efficient or proper
to use something more intensive. So
then, after each of these after the
drone kind of realizes that there's a
fire at a certain point, this is
determined when
the second YOLO model
um takes [clears throat] takes each
image, and once it detects a fire for
five consecutive
so it on that
it'll capture a proper footage, and
it'll feed it direct-
And we can see that there's not a
because while the drone is flying to the
next fire point, Cosmos
what? So, we decided that we'd
bottleneck wherever Cosmos is slow in
the time when it's anyways flying to the
next fire point. So, we don't have
actually have to wait for anything or
have slowdowns.
all five of these, and if there were if
there were more, that would be fine as
well. And we'd kind of rank them in
terms of the different metrics, like are
there people there, how intense is the
fire, how much is the smoke, are there
buildings collapsed, and a lot of
metrics.
And um
something that I would like to talk
about that was sort of interesting was
kind of how we went from
directions to 3D projections, right? So,
we initially have
high-level RGB photos that we take from
each frame, and we feed it to our YOLO
model, and it and it tells whether
there's a fire in this frame or not. And
we have five consecutive frames, we have
to feed something to a Cosmos reason
model.
And we can't just feed the 2D
information to Cosmos, because if you
consider a flat 2D image, it's really
not
tell much about the fire intensity. So,
what we needed to do was integrate an
additional depth camera to our drone.
And we have we actually have four
cameras, and the two most important ones
are the main RGB one and the depth one.
So, we take input from both of these. We
kind of put them together. We multiply
by a certain matrix. We and then we do a
linear transformation to this, and we
are able to get an appropriate 3D image
of the entire
um situation at that point. And then we
can feed this to our Cosmos reason model
with a specific JSON prompt with all of
the information that we have, and then
we can get a proper answer. So, having
this kind of 2D to 3D thing was a kind
of interesting problem. We learned a lot
from it, and it actually proved to be
really useful, because just having 2D
setups were not cutting it.
And something that we wish to extend
this further is this is just one drone,
right? And obviously, when we're having
a large-scale fire, we really need
multiple drones and a whole kind of
swarm setup, which essentially is
multiple drones flying around
communicating
and
optimizing the path that they take, so
that we're not spending too much
stuff.
So, what we want is
our goal eventually is is to have this
entire
and have a communication layer, so we
can better respond to fires and
um eventually create a better solution.
Very cool. And on that note, we've got
an interesting question coming in from
YouTube. Uh
uh can this be generalized to other use
cases? What do you guys have you guys
thought about that as well?
Yeah, so actually, we did some
experimentation. We were we first
started off with the wildfire situation,
but the data set that we used it
actually included a lot of different
situations like floods, hurricanes,
tornadoes, a lot of other different
natural disasters. So, we can we can
broaden this idea into different natural
disasters, other use cases, for example.
And uh for example, like in the case of
a flood, getting all those collapsed
buildings, and um same same thing,
tracking where people are being stuck,
where people are
not able to get to safety, and
yeah, just execute
it from there.
Very cool. And um can people access this
work anywhere? We got a question in the
comment asking about that. Um or are you
are you sharing it yet or no?
Well, yeah, the GitHub
GitHub is public, and it should I
believe it is linked on the
Is it LinkedIn? It's linked on the
LinkedIn post that came out with the
announcement of the winners, but also,
if it if you'd like, we can send it
through one of the chats in the YouTube
or LinkedIn stream to make it easily
accessible for the for the viewers.
>> Great. We we I think our one of our
producers can do that in the background.
So, um that's great. So, uh
this comment came in
We really want to go through it. It's
amazing. Maybe we can do something like
such a project here in Europe.
So, that's very cool. Thanks for that
request. We will put that GitHub link in
the chat.
Very cool.
Let me see. I'm looking at time. We'll
do one more question. This is coming
also from LinkedIn from Richard.
How do you think about accountability
when perception reasoning navigation
prioritization is split across different
components?
That's a big question.
Any thoughts on that?
So, this is
actually where agentic AI research kind
of
is kind of exploring and trying to solve
problems in this area. It's kind of when
there's multiple models or multiple
parts of an AI model that are kind of
working together. And what's what's kind
of interesting about this is you can The
way I like to think of this is kind of
like an optimization problem. So, you
have different things competing for
different resources, right? If you have
like multiple agents competing for
different resources, what you finally
want to do is make sure there's not
starvation agents. And also what you
want to make sure is that the final goal
is
accomplished.
So, this is obviously something that's
actively being studied. And I think if
we look into some of these research a
little bit more and understand how the
math works out between multiple agents
and resource allocation, it can be
directly applied to this project,
especially if we if we split Right now,
it's kind of just one one model focusing
on everything, right? We want to make it
more robust. We can have specialized
models for different aspects. And having
the competition between them, it can be
better used if we have this this kind of
idea, this agentic competing idea.
Very cool. And I see we have a very
special viewer.
This is John Mitchell,
an ambassador. Great stuff, guys.
Congrats on the big win.
He
worked with BMW for years
working on the digital twins and and
robotics. So, you have a fan there. But
John Mitchell,
let me see if I know we're running short
on time, but I see another good question
here really quick. Um
This is coming from YouTube.
From one of the one of the fellow
winners.
What what aspects would you further
enhance if you had more time?
I think like like we talked about,
right? We would want to have a
multi-drone setup ideally, which is
something that would definitely speed up
how we can access fires and you know,
prioritize resources.
And Andrew, you want to talk a little
bit more?
>> Yeah, I think if we can create just more
realistic environments like
the bottleneck as the state was saying
for like different
applications, different disasters is
that we just didn't have simulation data
or simulation environments to actually
test those in.
So, I think if we had more time, we can
just create better more hyperrealistic
environments, better animations. So, the
drone just has more things to test with.
And even getting more compute, we can
apply NVIDIA's Isaac Lab, Isaac Sim and
try to just train in different ways, see
what works best.
And that's kind of why we like these
competitions a lot because it tells us
like what what resource
really good for us to use. And also
where some things are potentially
lacking in areas that we could work on
and actually
friends. So, we would not have realized
like this deficiency and thought about
this problem unless we got went through
with this competition. So, we'd really
like to just thank you guys for helping
us.
>> Well, thank you thank you for being part
of it. I think you're making an impact
already. Inspiring a lot of the
developers watching this live stream for
sure.
We did post I don't expect people to
memorize this link, but I'm just putting
it on the screen so everybody can see
it. We did post in the chat where you
can get all the GitHub links. We'll also
update the video description with this
link so you can watch it afterwards. But
we posted that also on LinkedIn as well.
I can't thank you all for joining us.
It's been fascinating speaking to each
of you and hearing about your
involvement in this case across the
board.
Um
What advice do you have? Look, it sounds
like you you guys enjoy doing hackathons
and and team projects like this. What
advice would you have for developers
that are just diving in right now? Where
should they start?
I think
developers should just
take
take projects slow, take it one piece at
a time and tackle one problem plan out
projects well, have a set idea on what
it was because we took We took a very
long time just planning out our idea.
Exactly which tools we're going to use,
exactly who's going to do what.
Compartmentalize
huge part of our project so we're not
each other's toes.
So,
the thing is planning everything out,
knowing
you're going to do and have a set idea
of that. And then of course, doing lots
of research. Research on what you need,
what to what tools you're going to use.
And once you have a set plan, it's a lot
easier to then attack
attack your project and you'll be more
organized in the way and it's going to
turn out to be a much better product at
the very end.
I love it. You guys And you
you're getting some amazing Go ahead.
I'm sorry.
No, I was just going to say the
importance of small scale testing
before you branch it out. Because And
using other plentiful resources like
there's so much documentation about
everything today that just being able to
to to scale to be able to get through
this documentation, analyze it,
understand it and
one thing that a developer should use to
their advantage and
learn really really deeply while
developing their own products and apps.
Well, that is great advice. Thank you so
much. It's great comments still coming
in. Great to see college students trying
to build things to help society. Thank
you. Another comment coming from
LinkedIn. Very interesting. Thanks for
sharing.
Again, I can't thank you enough for
participating. Congratulations.
I can see why you guys did so well in
this contest. So,
so thanks for joining and hope to see
you in the community.
I think we're going to move on to our
our final winner here. Team LiveKit's
going to join us. Keep the questions
coming in. As you see, we're we're
tackling them in real time. David and
Bing, thank you so much for joining us
today. It's so nice to have you here.
Introduce yourselves first and tell me
about what your role was on the project
and then we'll talk about what the
project was.
Thanks for having us. We're super
excited to work on this project. I'm
David. I work on robotics at LiveKit.
Hey guys. Bing. Same thing. Work on
robotics at LiveKit.
Okay, great. Okay, well, so glad to have
you. Now, let's get into the meat of it.
What did you guys do?
Yeah, so what we built was
we So, what what we work on at LiveKit
is
building open source frameworks for
building agents that work with audio,
video and robotics.
So, for this we use Cosmos reasoning as
kind of the the brains to look at a lot
of video streams at the same time to
understand what's happening and
building a voice interface on top of
that. So, a human operator who is
who can monitor a bunch of video streams
can ask it questions,
look at what's happening in all the
streams because a human can't possibly
consume all these things at the same
time and monitor for them to look for
specific things,
specific objects and what's happening in
the scenes.
Very cool. All right, and you guys have
a little demo you want to show off,
right?
Hey, can you help me monitor some video
streams?
Absolutely. Please let me know which
feeds you'd like to monitor or what
specific content or events you want me
to watch for in the video streams. What
feeds do you have access to?
I have access to three feeds, street,
downstairs and upstairs. Which one would
you like to monitor or switch to? Or do
you want me to monitor something
specific across them? Can you switch to
the upstairs feed?
Switch to the upstairs feed. Would you
like me to keep monitoring it or do
anything else? Can you describe the
upstairs feed?
The upstairs feed shows a cozy room with
a large brown couch, a striped gray and
white rug, a wooden shelf cluttered with
books and containers and a piano near
the window. There's a woman sitting on
the floor in front of the couch holding
a baby suggesting a warm family setting.
The room has modern elements like
abstract green and black artwork above
the couch and a lamp near the window.
The woman is engaged in a tender moment
with the baby.
Would you like me to focus on anything
specific here or switch to another feed?
Can you monitor all feeds for any cars?
I am now monitoring all feeds for any
cars. I will automatically switch to the
feed if a car appears.
Let me know if you want to stop
monitoring or need anything else.
Switching to street. Can you stop all
monitoring?
I have stopped monitoring all feeds for
cars. Let me know if you want to monitor
anything else or need further
assistance. Can you monitor all feeds
for a computer?
I am now monitoring all feeds for any
computers. I will auto switch to the
feed if a computer appears. Let me know
if you want to stop monitoring or need
further assistance. Switching to
downstairs.
Very cool. Very cool. Wow, that is
pretty amazing actually.
Much easier to
navigate than a lot of apps that people
have with all their feeds.
Very interesting. I hadn't seen
something like that because we have a
couple of great questions already coming
in.
Let me see here
Here's one coming in from LinkedIn it
looks like. Any insights on tokens and
chunking for precision?
If you don't
If you you more information or not a
good question we can we can move to the
next one.
Yeah, I'm not sure what the question is
about
exactly.
All right, maybe if you want to clarify
that question we'll try to circle back
to you. Okay, another question coming
regarding the voice. The voice was GPT.
How did you find it versus other voice
agents?
The voice
I can't remember which model we used but
we built that around the the LiveKit
voice agents framework so it makes it
super easy to kind of plug in any voice
models and LLMs that you need.
Very cool and I'm getting a note from my
producer. Do you guys also have a
presentation deck available?
We don't. We could
What I wanted to just show was we have
some diagrams on
on the repo that I want to put up. Yeah,
very cool.
Again, these links are available. We'll
put them in the chat or in the
description afterwards so you can access
their work.
Okay, here's let me see.
There's a thing if you want to talk a
little bit about Yep, we see it there.
Yeah, I can give a bit more context. So
at first we just have this very simple
idea that current AI system right now
just really ingest one data stream at
one time either through chat interface
or you really have one video stream
which you ask about which you can see
like in other teams demo as well.
And we have this simple
hypothesis like what if AI just scale
and have to ingest multiple like
multiple data streams at once for
example video in this use cases like for
example what if there's a real time like
live show that an AI will direct
entirely with like five to 10 camera
streams. How can it do that? Or like in
a
enterprise building with hundreds of
cameras. How can it exactly be
a modern system that will pinpoint risks
immediately when it see ones?
And we just set out and try to build a
system that can do that with LiveKit
infrastructure.
What it really does is leveraging WebRTC
and some abstraction we built on top of
it. For example, each camera would have
a LiveKit client that connects to a
talking room just like the one we're in
right now.
And an orchestrator will look at every
single video stream and audio stream
and push that job to look at those and
analyze those to video workers and audio
workers
that look at the video stream, analyze
the camera, maybe um summarize it with
NVIDIA Cosmos
or just like look at the audio stream
and run a speech to text model that
takes this transcription
and put it into a database somewhere.
And at the end of the day we have a
system that can reliably scale to like
dozens of video stream. Like in our demo
we show like three or four but it really
can go much more.
And you can do stuff like just tell it
to let's say
um switch to a screen that has a certain
character, a certain object or even like
track across different screens like
hey, you have
a main character going from camera A to
camera B. Could you just look at them or
like if I have this storyline, I want to
mm
show like if for example on Netflix like
Too Hot to Handle or something like show
an affair, like show a show an
interesting viewpoint and you can do all
that with our architecture. It's really
scalable and at the end of the day it's
really easy to build as well. So what do
we want to highlight just
if you handle the infrastructure
correctly
any abstraction that's built upon of it
will be super simple and you can let
anything
handle it like an agent.
And yeah, this like the downstream task
for those agents will be ultra simple.
Nothing complex here.
Very interesting and we got a great
comment coming in a question.
Yeah, [clears throat] this is from
Richard. In a multi-camera setting what
turned out to be harder, perception,
cross-stream memory or deciding which
observations actually matter?
It's a good one.
Mm.
I would think that there's a lot of
things that we thought would be hard
like for example cross-stream memory but
as it turns out like once we kind of see
how to even like orchestrate these video
workers without like
having them conflicting with each other
or like having really performance
bottleneck on the server
it it really just works as soon as you
try to push
like these summarization into a vector
database as long as the vector database
can handle it as long as you do a good
harness of the agent so it can know how
to search for these
like summarization snippets
yeah, it just it would just
work.
At the end of the day I really just want
to stretch this out like as long as you
have a good harness, as long as you kind
of plan out
what a scalable infrastructure would
look like
but the LLM doesn't even matter
as long as it's a decently good one.
Very cool. Well, let me see. John
Mitchell is asking here how many camera
feeds do you think you can handle at one
time? Is there any
limitations? I guess this is kind of
dependent on on the hardware you're
using, right?
Yeah,
right now in terms of like LiveKit
limitations itself that we think we can
handle upwards of
a few hundred
different camera streams on our SFU.
David can correct me if I'm wrong on
this.
Probably more.
Yeah, it's probably up to the thousands.
Yeah.
>> Wow.
A million.
>> [laughter]
>> So wait, what's the
what's the environment you guys using
now based that that's based on?
For the WebRTC stack we just use our own
LiveKit cloud. Wow.
Yeah,
and for the
Yeah, for the ingestion downstream we
use Nebius with the LLM
Cosmos reason to be. And that's actually
the only bottleneck is that how can we
actually run inference on so many
these of these video streams at once and
I think we can reliably run up to 10
different video streams
with our current harness.
on a single H100.
Wow, could be super helpful. Okay,
that's great insight. Another question
coming in from LinkedIn. Can you train
objects that it didn't recognize and
train LLM to pick it up next time
around?
Definitely.
One of the
quirks of the architecture we built is
that you can really literally spawn any
kind of workers. We also have an example
at LiveKit where we just have a model
that just use YOLO to detect objects
and that can be spawned as a worker that
pushes data into a graph database
and
or just like other teams have done you
can fine-tune your LLMs or VLMs to
detect these objects. I don't really
have seen teams that fine-tune VLMs for
special object detection before but that
can definitely be done.
And realistically wouldn't be hard to
integrate into our current example at
all.
Very cool. Look at this.
I
another lots of great comments coming
in. I can't even I don't have time to
put them all on the screen. Um Let me
see. Here's a good question coming in
from our good friend on YouTube. What
are the tips to building such agents
using LLMs and vision language models?
Yeah, what kind of advice do you have
for devs? Looks like a lot of people
excited about this one.
I think the best tip
well, recently Claude just leaked their
code base. I think you can find a lot of
tips inside there.
But also
>> [laughter]
>> in terms of agent harnesses there are a
lot of papers that have been floating
around especially in robotics as well.
Agent harnesses are kind of hot topic.
For example, code policies.
All all these things you can probably
find on X if you follow robotics a lot
but one particular
resource I find very interesting
recently is a
Theo T3
dot GG. My guy. He posted a video where
he explained agent harnesses and it's
really
interesting resource on how you can
build an agent harness yourself and what
is the best tips
on how to do such thing.
Very cool. Another comment coming in
from YouTube saying LiveKit is just
awesome. I use it for live video capture
and include agents in the stream to
analyze including including Cosmos
Reason too.
Very cool. Thanks for that. Um Okay, I
think we're putting the links in the
chat. So I see people asking for those
links so one of our producers will add
it there. Wow, very cool. All right, let
me see. Someone's asking what vision
model are you using?
NVIDIA Cosmos.
Reason 2 to be.
2 to be.
Yeah. I said it earlier. Okay.
If anyone is tuning in late to the live
stream, if you don't watch it or you're
watching the replay, you can always go
back. This live stream will live on on
our YouTube channel. I think also on
LinkedIn. So feel free to watch it
again.
We'll try to answer some of these
questions in the chat also but I see
there's lots of great
lots of good comments here.
Um let me see.
Uh, okay, here's
I'll look try to see if there's another
one here. Question.
Oh, look at all all I'll take this one
for me, I think. How can we be part of
the community to learn new AI ideas
project being built and also participate
in a hackathon like this? Well, I think
one of the best ways is to actually be
involved in on our community Discord
server. We have two actually. In video
developer Discord
um, and we have the video Omniverse
Discord. Um, the way uh, you know which
where to go is if you're doing anything
with Omniverse, uh, that's the Omniverse
Discord server and anything else uh,
from Nvidia all the other APIs, SDKs and
everything that's all in the Nvidia
developer Discord. But feel free to to
ask your question one of those and one
of the admins will help you if if you
need to post that to the other one. Uh,
for this topic we actually have a nice
Cosmos category um, uh, of of channels
on the Nvidia Omniverse Discord server.
We'll post a link for that Discord
server there. I think um, you know,
I've seen so many great things come out
of engagement on the Discord server with
developers. Uh, whether it's just
chatting and learning about each other's
projects
uh, in for example on the Cosmos channel
or the Isaac Sim channel, whether
robotics chit chat channel, uh, the
introduction channel where you just talk
about your background. People always
chime in there. Uh, but also the
community uses the Discord to uh, to do
study groups. We actually have multiple
study groups where you can organize your
own or you can jump on one of the
existing study groups. We have a nice ed
event calendar where we list the current
study groups. Um, these are again
managed by community members and we just
list them in the calendar for
everybody's visibility. That's a great
way to engage with community and and
other developers. Um, and of course on
LinkedIn, I think LinkedIn is one of the
best places to uh, to engage with
developers. Do David, do you use
LinkedIn to post your your work and
updates? Yeah, absolutely.
Do you
do you Substack or any anywhere else you
recommend people go? Where do you get
your information from?
Uh, LinkedIn is great. X is also great
especially for robotics and AI.
Cool. What's your favorite what what's
your favorite follow on on X? Where do
you want people to go to?
Oh, man, there are so many.
Uh,
Let's see. Well, you can think about it.
Think about it for a minute. Yeah.
Okay. Um, but that's I think that's
that's great advice though. Um, and you
normally do you do you are you engaging
with the posters on there or are you
just using it to kind of uh,
get information from the feed?
Oh, I I love engaging with uh,
the posts especially if it's coming from
robotics researchers when they post new
papers.
Very cool. Well, listen, um, that's
great advice. I want to thank you both
representing. This has been fantastic.
Um, I'm really Each of these projects
very unique in their own right but very
innovative.
Uh, I think we really just saw some
exciting exciting projects as well this
hackathon. So, congratulations to each
of the winners. Um, um, I'm going to
we're going to shift now to talk about
Hey, there there there's team Jarvis.
Hey, team Jarvis. Um, I think anyone
like I said earlier, anyone who tuned in
a little late um, want to want to
definitely watch this from the
beginning.
Uh, we're going to chapterize it and
stuff but um,
we have just seen how developers are
pushing physical AI forward and
literally just four weeks uh, with this
hackathon. Uh, you just got to meet the
three teams that I think really set the
standard for future hackathons. Team
Zenith uh, took a nice place with
end-to-end palletizing system powered by
Cosmos Reason 2B and and lower fine
tuning. Uh, team Jarvis uh, followed up
with a great presentation on autonomous
disaster response drone which is built
leveraging Nvidia Isaac Sim
uh, and we just finished chatting with
team LifeKit placed by leveraging AI
driven video feed um, management across
multiple camera streams
uh, that you can engage with and
interact with in real time. Um, each of
you really well done. I uh, the uh, the
audience was very engaged throughout
because all of your your projects have
just been really revealing. So, thank
you all for coming on and
congratulations. You should be really
proud of the work you did. I can't wait
to see what you are all doing next with
your projects
um, and we'll be sure to follow you on
LinkedIn.
Um, so thank you for joining us today.
We're going to shift gears now and talk
about Cosmos. We're going to
uh, take a look back at some of the
recent announcements we had from GTC.
I'm going to bring my my colleague uh,
Panjali here is going to join us. Um,
and um, let me see if she's here in the
wings. There she is. Yeah, she is. Nice
project. But Panjali, was that amazing
or what?
Oh my god, so exciting and this was so
much fun
bringing all of this together with me.
We were planning for the cook-off and
then seeing all of these amazing
brilliant folks contributing to Cosmos
Cookbook and Cosmos Cook-Off is is might
be the highlight of what we have done.
Thank you so much everyone
and sharing your work with us. And
with that said, we have five minutes or
some time to just get into
what we brought in as the new Cosmos.
A lot of you already
worked on Cosmos Reason. So, this might
be exciting for you. For those who do
not know the Cosmos Cook-Off was
especially focused on Cosmos Reason
which is our visual language model. It
also does physical AI reasoning. So, all
of these projects that you saw were
built on Cosmos Reason and I'm going to
share my screen and we just going to go
by through bunch of updates and and
more. So, let me know if you can see my
screen.
>> Let me see.
Uh,
I'm looking for it.
Can you see it? I don't see it unless I
might need help from one of the
producers cuz All right, I see it. I see
it.
Okay, perfect. So,
uh, so this is
what our Cosmos Reason 8B uh, model
looks like. Cosmos Reason 2 8B model
look likes but the the recent update
that we got to this
model was actually we got a new name um,
which is
here.
Let me go through it quickly.
I'll put the link to this in the chat so
everyone can bring this up on their own.
Yep.
Just Okay, I'm going to share again.
I'm new to the sharing. It's okay. Let
me bring this back up.
>> [laughter]
>> Take your time and thanks for having
It's great to see everybody hanging out.
We've never had so many
so many people on the camera one time.
Uh,
>> Yeah.
So, one thing that that's new and we
released recently is Cosmos Reason 2 2B
and Cosmos Reason 2 8B NeM. If you don't
know about NeMs, NeMs are these
containerized optimized models that you
can run. So, if you are part of Nvidia
developer programs, what you can do is
you can go to
NGC catalog, look for Cosmos Reason 2B
and 8B NeM and get the container. So,
you know, you just go either create your
new account or sign in using your
developer accounts. And why this NeM is
important because it gives kind of 10X
improvements on the performance. And if
you're using one of the recent
checkpoints, it might give you up to 50X
speed bump ups on Cosmos Reason 2 VLM.
So, this is super exciting, super
important and this is all Nvidia is
about, right? We do
a lot of optimizations and we bring in
the best technologies
for people
to really run these models. And another
uh,
another such
you know, update is also the kind of
techniques that happen
for these models. And one of such
interesting techniques is Cosmos
distillation. So,
one
For those of you who don't know what
distillation is, distillation is kind of
taking this big model which we call a
teacher model that knows everything in
this world relate to that specific field
in world foundation model's case, the
teacher model is going to be the
generalized world foundation model. But
then you distill the knowledge of that
teacher model into small student models
and these student models are so fast as
inference because you have reduced the
number of inference steps from teacher
model while you were distilling for a
student model. So, we have released
Cosmos Predict 2 which is our world
generation model. We have released its
distilled code base on the GitHub. So,
you can go to Cosmos GitHub, go to
Cosmos Predict 2 and find this
distillation guide and run this
distillation model. This is going to
give you a lot of improvements on your
inference and lot of great speed bump
ups. So, again as I said, lots of
interesting updates on Cosmos.
So, you got to check out the
distillation guides that we have put out
for both Cosmos Predict 2.5 and Cosmos
Trans for 2.5. For those who work with
simulation to real kind of use cases,
all the Omniverse fam shout out to you.
You can go to Trans for 2.5 distillation
guide and check it out. Um, so great new
stuff coming out of GTC, great exciting
projects coming out of Cosmos Cook-Off.
So, I think we had a really shiny month.
So, huge round of applause for everyone.
Yes, absolutely. Thank you so much,
Panjali. That's really fantastic
information. Where Where should people
Where do you recommend people go for
support if they're working with it? They
want to go to the the GitHub issues area
or somewhere else? That's right. So,
I'll put links in the chat. These are
Cosmos GitHub. You can go and update as
issues, or you can tag us in Discord if
you're running through any technical
issues and you need some help. So, both
of those ways uh there's no wrong way to
do it.
Okay, great. And I also want to give a
special thank you to some people that
this live stream took some some
planning. Want to thank Xavi and and
Kristen and Zach who's been amazing
behind the scenes with posting all these
videos and and presentations. So, hats
off to the team, but major
congratulations to all the three teams
that are here and everybody who
participated in the hackathon. I can't
tell you how much we enjoyed seeing all
these projects, and you're all winners
to us. Uh so, I hope you participate in
the next one. Uh
and uh give us your feedback, too, if
there's anything you want to see us do
in the future. We're happy to hear it.
Um
and check out the EdEvents calendar for
next live streams. Jump on the Discord
server, whether it's the Media Developer
Discord or the Omniverse Discord server
if you want to chat with other
developers and leverage the uh the
GitHub pages, Pranjali said, for uh for
support. Thank you all. Good luck with
your work. We can't see uh we can't wait
to see what you all do next. Uh and
until next time, it's been a pleasure
having you today. Have a great rest of
the day.