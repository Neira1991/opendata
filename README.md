# Producing a unified graph representation from a match

## About this repo

### Description

This repo contains 9 matches of broadcast tracking data collected by [SkillCorner](https://skillcorner.com) and the idea is to produce a unified graph representation by each match.


### Motivation

This data has been open sourced in a joint initiative between [SkillCorner](https://skillcorner.com) and [Friends Of Tracking](https://www.youtube.com/channel/UCUBFJYcag8j2rm_9HkrrA7w). The goals are multiple:
* Provide access to tracking data to researchers and the sports analytics community.
* Increase awareness on the existence of broadcast tracking data, and how it can be of benefit to clubs, media and the betting industry.
* Allow SkillCorner prospects to access data easily, parse our data format and get started building on top of it.

Thus, if you use the data, we kindly ask that you credit SkillCorner and hope you'll notify us on [Twitter](https://twitter.com/skillcorner) so we can follow the great work being done with this data.

## Documentation

### Data Structure

The `data` directory contains:

* `matches.json` file with basic information about the match. Using this file, pick the `id` of your match of interest.
* `matches` folder with one folder for each match (named with its `id`).

For each match, there is two files:

* `match_data.json` contains lineup information, referee, pitch size...
* `structured_data.json` contains the tracking data (the players, the main referee and the ball).



### Limitation

The data has been processed as SkillCorner produced matches from over 20 leagues (more than 8000 matches this season). The data has been collected automatically from the broadcast and has not received any manual correction. What it means for user:

* The data is limited to what is visible on the broadcast video. Not all the players are visible (thus included in the data) all the time. The broadcast show an average of 14 players out of 22 at each frame. During replays or close up views, the data is not included.
* Some data points are erroneous. Around 95% of the player identity we provide are accurate. For the missing 5%, the identity of the player may be missing (we only provide the `group_name`), or the identity can be provided, but wrong.
* Some speed or acceleration smoothing and control should be applied to the raw data.


## Contact us

* If you have some feedback, reach us on  [Twitter](https://twitter.com/JStevenNeira)
