import csv
# Read the data from the CSV file
csv_file = "37th_Early_Bird_Open_Mens_5000_Meters_HS_Open_5K_24.csv"
output_file = "37th_Early_Bird_Open_Mens_5000_Meters_HS_Open_5K_24.html"
# Open the CSV file and extract the data
with open(csv_file, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)


# Extract the data from the CSV
meet_name = data[0][0]  # Column A - h1 (Meet Name)
meet_date = data[1][0]  # Column B - h2 (Meet Date)
team_results_link = data[2][0]  # Column C - hyperlink for the team-results section
# folder_name = data[1][3]  # Column D - folder name used in photo-gallery links
race_comments = data[3][0]  # Column E - race-comments section

early_bird_html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel = "stylesheet" href = "css/reset.css">
    <link rel = "stylesheet" href = "css/style.css">
    <title>{meet_name} Country Meet</title>
</head>
<body>
    <header>
        <h1>{meet_name}</h1>
        <h2>{meet_date}</h2>
    </header>
    <!-- Section for overall team results -->
    <section id="team-results">
        <h2>Overall Team Results</h2>
        <p><a href="{team_results_link}">Team results are available here.</a></p>
    </section>

    <!-- Section for Team Placements -->
    <section id="team-placements">
        <h2>Team Placements</h2>
        <table id="team-table">
            <thead>
                <tr>
                    <th>Placement</th>
                    <th>Team Name</th>
                    <th>Score</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>1</td>
                    <td>Holly</td>
                    <td>79</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>Canton</td>
                    <td>133</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>Midland</td>
                    <td>145</td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>Oxford</td>
                    <td>148</td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>Plymouth</td>
                    <td>169</td>
                </tr>
                <tr>
                    <td>6</td>
                    <td>Salem</td>
                    <td>201</td>
                </tr>
                <tr>
                    <td>7</td>
                    <td>Lake Orion</td>
                    <td>213</td>
                </tr>
                <tr>
                    <td>8</td>
                    <td>Troy</td>
                    <td>215</td>
                </tr>
                <tr>
                    <td>9</td>
                    <td>Howell</td>
                    <td>218</td>
                </tr>
                <tr>
                    <td>10</td>
                    <td>Dexter</td>
                    <td>243</td>
                </tr>
                <tr>
                    <td>11</td>
                    <td>Davison</td>
                    <td>293</td>
                </tr>
                <tr>
                    <td>12</td>
                    <td>Midland Dow</td>
                    <td>309</td>
                </tr>
                <tr>
                    <td>13</td>
                    <td>Ann Arbor Skyline</td>
                    <td>349</td>
                </tr>
                <tr>
                    <td>14</td>
                    <td>Detroit Catholic Central</td>
                    <td>353</td>
                </tr>
                <tr>
                    <td>15</td>
                    <td>Utica Eisenhower</td>
                    <td>358</td>
                </tr>
                <tr>
                    <td>16</td>
                    <td>Romeo</td>
                    <td>431</td>
                </tr>
                <tr>
                    <td>17</td>
                    <td>Rochester Adams</td>
                    <td>437</td>
                </tr>
                <tr>
                    <td>18</td>
                    <td>Hartland</td>
                    <td>460</td>
                </tr>
                <tr>
                    <td>19</td>
                    <td>New Baltimore Anchor Bay</td>
                    <td>472</td>
                </tr>
                <tr>
                    <td>20</td>
                    <td>Utica Ford</td>
                    <td>483</td>
                </tr>
                <tr>
                    <td>21</td>
                    <td>Livonia Stevenson</td>
                    <td>508</td>
                </tr>
                <tr>
                    <td>22</td>
                    <td>Grand Blanc</td>
                    <td>552</td>
                </tr>
                <tr>
                    <td>23</td>
                    <td>Clinton Twp. Chippewa Valley</td>
                    <td>564</td>
                </tr>
                <tr>
                    <td>24</td>
                    <td>Troy Athens</td>
                    <td>680</td>
                </tr>

            </tbody>
            </table>
    </section>
    <!-- Section for Top Athletes -->
    <section id="Top-Athletes">
        <h2>Top 5 Athletes</h2>
        <table id="athlete-table">
        <thead>
        <tr>
            <th>Placement</th>
            <th>Grade</th>
            <th>Athlete Name</th>
            <th>Athlete Link</th>
            <th>Time</th>
            <th>School Name</th>
            <th>Team Link</th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <td>1</td>
            <td>10</td>
            <td>Jack MacGregor</td>
            <td><a href="https://www.athletic.net/athlete/17456114/cross-country">Link</a></td>
            <td>15:41.2</td>
            <td>Howell</td>
            <td><a href="https://www.athletic.net/athlete/17456114/cross-country">Link</a></td>
        </tr>
        <tr>
            <td>2</td>
            <td>11</td>
            <td>Aiden Pengelly</td>
            <td><a href="https://www.athletic.net/athlete/21144396/cross-country">Link</a></td>
            <td>15:45.8</td>
            <td>Canton</td>
            <td><a href="https://www.athletic.net/athlete/21144396/cross-country">Link</a></td>
        </tr>
        <tr>
            <td>3</td>
            <td>12</td>
            <td>Kian Schneeweis</td>
            <td><a href="https://www.athletic.net/athlete/19825394/cross-country">Link</a></td>
            <td>15:56.6</td>
            <td>Troy</td>
            <td><a href="https://www.athletic.net/athlete/19825394/cross-country">Link</a></td>
        </tr>
        <tr>
            <td>4</td>
            <td>12</td>
            <td>Alexander McArthur</td>
            <td><a href="https://www.athletic.net/athlete/22186133/cross-country">Link</a></td>
            <td>16:03.0</td>
            <td>Oxford</td>
            <td><a href="https://www.athletic.net/athlete/22186133/cross-country">Link</a></td>
        </tr>
        <tr>
            <td>5</td>
            <td>12</td>
            <td>Julian Linebaugh</td>
            <td><a href="https://www.athletic.net/athlete/17349252/cross-country">Link</a></td>
            <td>16:08.7</td>
            <td>Dexter</td>
            <td><a href="https://www.athletic.net/athlete/17349252/cross-country">Link</a></td>
        </tr>
        </tbody>
        </table>
    </section>
    '''
# output_file = f"{meet_name.replace(' ', '_').lower()}.html"
with open("Early_Bird.html", 'w') as file:
    file.write(early_bird_html_content)


# new file here

csv_file = "56th_Holly-Duane_Raffin_Festival_of_Races_Mens_5000_Meters_D1_Boys_24.csv"
# Open the CSV file and extract the data
with open(csv_file, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)


# Extract the data from the CSV
meet_name = data[0][0]  # Column A - h1 (Meet Name)
meet_date = data[1][0]  # Column B - h2 (Meet Date)
team_results_link = data[2][0]  # Column C - hyperlink for the team-results section
# folder_name = data[1][3]  # Column D - folder name used in photo-gallery links
race_comments = data[3][0]  # Column E - race-comments section

holly_duane_html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel = "stylesheet" href = "css/reset.css">
    <link rel = "stylesheet" href = "css/style.css">
    <title>{meet_name} Country Meet</title>
</head>
<body>
    <header>
        <h1>{meet_name}</h1>
        <h2>{meet_date}</h2>
    </header>
    <!-- Section for overall team results -->
    <section id="team-results">
        <h2>Overall Team Results</h2>
        <p><a href="{team_results_link}">Team results are available here.</a></p>
    </section>

    <!-- Section for Team Placements -->
    <section id="team-placements">
    <h2>Team Placements</h2>
        <table id="team-table">
            <thead>
                <tr>
                    <th>Placement</th>
                    <th>Team Name</th>
                    <th>Score</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>1</td>
                    <td>Holly</td>
                    <td>79</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>Canton</td>
                    <td>133</td>
                </tr>
                <tr>
                    <td>3</td>
                    <td>Midland</td>
                    <td>145</td>
                </tr>
                <tr>
                    <td>4</td>
                    <td>Oxford</td>
                    <td>148</td>
                </tr>
                <tr>
                    <td>5</td>
                    <td>Plymouth</td>
                    <td>169</td>
                </tr>
                <tr>
                    <td>6</td>
                    <td>Salem</td>
                    <td>201</td>
                </tr>
                <tr>
                    <td>7</td>
                    <td>Lake Orion</td>
                    <td>213</td>
                </tr>
                <tr>
                    <td>8</td>
                    <td>Troy</td>
                    <td>215</td>
                </tr>
                <tr>
                    <td>9</td>
                    <td>Howell</td>
                    <td>218</td>
                </tr>
                <tr>
                    <td>10</td>
                    <td>Dexter</td>
                    <td>243</td>
                </tr>
                <tr>
                    <td>11</td>
                    <td>Davison</td>
                    <td>293</td>
                </tr>
                <tr>
                    <td>12</td>
                    <td>Midland Dow</td>
                    <td>309</td>
                </tr>
                <tr>
                    <td>13</td>
                    <td>Ann Arbor Skyline</td>
                    <td>349</td>
                </tr>
                <tr>
                    <td>14</td>
                    <td>Detroit Catholic Central</td>
                    <td>353</td>
                </tr>
                <tr>
                    <td>15</td>
                    <td>Utica Eisenhower</td>
                    <td>358</td>
                </tr>
                <tr>
                    <td>16</td>
                    <td>Romeo</td>
                    <td>431</td>
                </tr>
                <tr>
                    <td>17</td>
                    <td>Rochester Adams</td>
                    <td>437</td>
                </tr>
                <tr>
                    <td>18</td>
                    <td>Hartland</td>
                    <td>460</td>
                </tr>
                <tr>
                    <td>19</td>
                    <td>New Baltimore Anchor Bay</td>
                    <td>472</td>
                </tr>
                <tr>
                    <td>20</td>
                    <td>Utica Ford</td>
                    <td>483</td>
                </tr>
                <tr>
                    <td>21</td>
                    <td>Livonia Stevenson</td>
                    <td>508</td>
                </tr>
                <tr>
                    <td>22</td>
                    <td>Grand Blanc</td>
                    <td>552</td>
                </tr>
                <tr>
                    <td>23</td>
                    <td>Clinton Twp. Chippewa Valley</td>
                    <td>564</td>
                </tr>
                <tr>
                    <td>24</td>
                    <td>Troy Athens</td>
                    <td>680</td>
                </tr>

            </tbody>
            </table>
    </section>

    <!-- Section for Top Athletes -->
    <section id="Top-Athletes">
        <h2>Top 5 Athletes</h2>
        <table id="athlete-table">
        <thead>
        <tr>
            <th>Placement</th>
            <th>Grade</th>
            <th>Athlete Name</th>
            <th>Athlete Link</th>
            <th>Time</th>
            <th>School Name</th>
            <th>Team Link</th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <td>1</td>
            <td>10</td>
            <td>Jack MacGregor</td>
            <td><a href="https://www.athletic.net/athlete/17456114/cross-country">Link</a></td>
            <td>15:41.2</td>
            <td>Howell</td>
            <td><a href="https://www.athletic.net/athlete/17456114/cross-country">Link</a></td>
        </tr>
        <tr>
            <td>2</td>
            <td>11</td>
            <td>Aiden Pengelly</td>
            <td><a href="https://www.athletic.net/athlete/21144396/cross-country">Link</a></td>
            <td>15:45.8</td>
            <td>Canton</td>
            <td><a href="https://www.athletic.net/athlete/21144396/cross-country">Link</a></td>
        </tr>
        <tr>
            <td>3</td>
            <td>12</td>
            <td>Kian Schneeweis</td>
            <td><a href="https://www.athletic.net/athlete/19825394/cross-country">Link</a></td>
            <td>15:56.6</td>
            <td>Troy</td>
            <td><a href="https://www.athletic.net/athlete/19825394/cross-country">Link</a></td>
        </tr>
        <tr>
            <td>4</td>
            <td>12</td>
            <td>Alexander McArthur</td>
            <td><a href="https://www.athletic.net/athlete/22186133/cross-country">Link</a></td>
            <td>16:03.0</td>
            <td>Oxford</td>
            <td><a href="https://www.athletic.net/athlete/22186133/cross-country">Link</a></td>
        </tr>
        <tr>
            <td>5</td>
            <td>12</td>
            <td>Julian Linebaugh</td>
            <td><a href="https://www.athletic.net/athlete/17349252/cross-country">Link</a></td>
            <td>16:08.7</td>
            <td>Dexter</td>
            <td><a href="https://www.athletic.net/athlete/17349252/cross-country">Link</a></td>
        </tr>
        </tbody>
        </table>
    </section>
    '''
# output_file = f"{meet_name.replace(' ', '_').lower()}.html"
with open("Holly_Duane.html", 'w') as file:
    file.write(holly_duane_html_content)

# third file here

csv_file = "Bret_Clements_Bath_Invitational_Mens_5000_Meters_Class_1_24.csv"
# Open the CSV file and extract the data
with open(csv_file, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)


# Extract the data from the CSV
meet_name = data[0][0]  # Column A - h1 (Meet Name)
meet_date = data[1][0]  # Column B - h2 (Meet Date)
team_results_link = data[2][0]  # Column C - hyperlink for the team-results section
# folder_name = data[1][3]  # Column D - folder name used in photo-gallery links
race_comments = data[3][0]  # Column E - race-comments section

bret_clements_html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel = "stylesheet" href = "css/reset.css">
    <link rel = "stylesheet" href = "css/style.css">
    <title>{meet_name} Country Meet</title>
</head>
<body>
    <header>
        <h1>{meet_name}</h1>
        <h2>{meet_date}</h2>
    </header>
    <!-- Section for overall team results -->
    <section id="team-results">
        <h2>Overall Team Results</h2>
        <p><a href="{team_results_link}">Team results are available here.</a></p>
    </section>

    <!-- Section for Team Placements -->
    <section id="team-placements">
        <h2>Team Placements</h2>
        <table id="team-table">
        <thead>
            <tr>
                <th>Placement</th>
                <th>Team Name</th>
                <th>Score</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1</td>
                <td>Chuck Block Timing</td>
                <td>20</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Northville</td>
                <td>62</td>
            </tr>
            <tr>
                <td>3</td>
                <td>Saline</td>
                <td>105</td>
            </tr>
            <tr>
                <td>4</td>
                <td>Okemos</td>
                <td>147</td>
            </tr>
            <tr>
                <td>5</td>
                <td>Ann Arbor Skyline</td>
                <td>152</td>
            </tr>
            <tr>
                <td>6</td>
                <td>Ann Arbor Huron</td>
                <td>157</td>
            </tr>
            <tr>
                <td>7</td>
                <td>DeWitt</td>
                <td>182</td>
            </tr>
            <tr>
                <td>8</td>
                <td>Holly</td>
                <td>209</td>
            </tr>
            <tr>
                <td>9</td>
                <td>Fenton</td>
                <td>232</td>
            </tr>
            <tr>
                <td>10</td>
                <td>East Lansing</td>
                <td>249</td>
            </tr>
            <tr>
                <td>11</td>
                <td>Flushing</td>
                <td>327</td>
            </tr>
        </tbody>
        </table>
    </section>
    
    <!-- Section for Top Athlete Placements -->
    <section id="athlete-placements">
        <h2>Top 5 Athletes</h2>
        <table id="athletes-table">
        <thead>
            <tr>
            <th>Placement</th>
            <th>Grade</th>
            <th>Athlete Name</th>
            <th>Athlete Link</th>
            <th>Time</th>
            <th>Team Name</th>
            <th>Team Link</th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <td>1</td>
            <td>12</td>
            <td>Ethan Powell</td>
            <td><a href="https://www.athletic.net/athlete/17514447/cross-country">Link</a></td>
            <td>15:55.20</td>
            <td>Northville</td>
            <td><a href="https://www.athletic.net/athlete/17514447/cross-country">Link</a></td>
        </tr>
        <tr>
            <td>2</td>
            <td>11</td>
            <td>Ben Hartigan</td>
            <td><a href="https://www.athletic.net/athlete/21351035/cross-country">Link</a></td>
            <td>16:11.63</td>
            <td>Northville</td>
            <td><a href="https://www.athletic.net/athlete/21351035/cross-country">Link</a></td>
        </tr>
        <tr>
            <td>3</td>
            <td>11</td>
            <td>Ian Morgan</td>
            <td><a href="https://www.athletic.net/athlete/20362252/cross-country">Link</a></td>
            <td>16:17.20</td>
            <td>Okemos</td>
            <td><a href="https://www.athletic.net/athlete/20362252/cross-country">Link</a></td>
        </tr>
        <tr>
            <td>4</td>
            <td>10</td>
            <td>Brandon Cloud</td>
            <td><a href="https://www.athletic.net/athlete/18566554/cross-country">Link</a></td>
            <td>16:18.07</td>
            <td>Northville</td>
            <td><a href="https://www.athletic.net/athlete/18566554/cross-country">Link</a></td>
        </tr>
        <tr>
            <td>5</td>
            <td>12</td>
            <td>Theodore Davis</td>
            <td><a href="https://www.athletic.net/athlete/16019015/cross-country">Link</a></td>
            <td>16:21.37</td>
            <td>Dansville</td>
            <td><a href="https://www.athletic.net/athlete/16019015/cross-country">Link</a></td>
        </tr>
        </tbody>
        </table>
        </section>
    '''
# output_file = f"{meet_name.replace(' ', '_').lower()}.html"
with open("Bret_Clements.html", 'w') as file:
    file.write(bret_clements_html_content)

