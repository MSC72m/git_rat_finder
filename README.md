# git_rat_finder

## What It Does

### Automatic Rat Detection and Removal
Detects users who follow you, whom you follow back, and then sneakily unfollow you. Git Rat Finder swiftly unfollows these social media "rats."

### Follower and Following Lists
Generates comprehensive lists of your followers and followings, making it easier to see who’s still in the game.

### Bulk and Manual Operations
Whether you prefer a swift, sweeping action or a meticulous manual approach, Git Rat Finder has got you covered. Follow or unfollow users in bulk or one by one.

## Why It's Great

### Saves Time
Automates the tedious task of managing followers and followings.

### Keeps Your Feed Clean
Ensures you’re only following those who reciprocate your interest.

### User-Friendly
Simple to use with clear instructions, even if you’re not a coding wizard.

### Open Source
Tweak it, improve it, make it your own. The code is yours to play with.


## Features

**Git Rat Finder** comes with the following features:

- **Unfollow Rats:** Automatically unfollow users who have unfollowed you after you followed them back.
- **Fetch Lists:**
  - **Followers List:** Retrieve a list of your current followers.
  - **Following List:** Retrieve a list of users you are currently following.
- **Bulk Operations:**
  - **Bulk Follow:** Follow a list of users in one go.
  - **Bulk Unfollow:** Unfollow a list of users all at once.
- **Manual Management:**
  - **Manual Follow:** Follow users one by one from a list.
  - **Manual Unfollow:** Unfollow users one by one from a list.
- **Detailed Reports:** Generate and display detailed reports of followers and followings.


## Installation

**Clone the repository**:
   ```sh
   git clone https://github.com/MSC72m/git_rat_finder.git
   cd git_rat_finder
   ```
Create a virtual environment (optional but recommended):

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
**Install Required Libraries:**
```sh
    pip install -r requirements.txt
```
## Usage
Run the application:
```bash
cd git_rat_finder
python main.py
```
Enter desired option

## Requirements

- Python 3.x
- Required libraries:
  - `asyncio`
  - `httpx`
  - `time`

## Troubleshooting

### Network Issues
If you happen to encounter network-related errors, please make sure you have a stable internet connection and try again.

### Error Messages
Error messages will be displayed in a terminal if any issues occur during the process. Please take a look at these messages to understand what went wrong.

## Contributing

We welcome contributions to **Git Rat Finder**! Here's how you can help:
Contributions are welcome! Please create an issue or submit a pull request for any improvements or new features.
