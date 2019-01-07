# jrl-umi3218 Robotics Tasks Repositories

For the real time control of robot kinematic chains, see https://github.com/jrl-umi3218/Tasks for details.

This Repository is a super-repository containing a consistent set of key robotics tasks repositories from the original repositories at [https://github.com/jrl-umi3218/](https://github.com/jrl-umi3218/), so that changes can be made in a consistent way which will compile at every key commit in the branches `master` and `grl`.
The upstream clone location of all repositories in this super-repository is `github.com/ahundt/* -b grl`.

Build this code with https://github.com/ahundt/robotics_setup/blob/master/robotics_tasks.sh.

Tested on Ubuntu 14.04, 16.04 and MacOS.

Primary repository subtrees were added with commands like the following:

    git subtree add --prefix eigen-qld https://github.com/ahundt/eigen-qld.git grl

cmake subtrees in `jrl-umi3218/*/cmake` were added with the command:

    git subtree add --prefix cmake https://github.com/ahundt/jrl-cmakemodules python