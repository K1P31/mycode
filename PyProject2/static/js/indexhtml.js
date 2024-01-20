let tournaments = [
  [
    "Milan, Italy",
    "Milan",
    "https://www.ibjjfdb.com/Championship/Logo/2425",
  ],
  [
    "Europe",
    "Europe",
    "https://www.ibjjfdb.com/Championship/Logo/2342",
  ],
  [
    "San Jose, CA",
    "SanJose",
    "https://www.ibjjfdb.com/Championship/Logo/2368",
  ],
];

let tournament_cards_container = document.getElementById('tournament_cards_container');

function createTournamentCards(tournaments) {
  tournaments.forEach((elt, i) => {
    let location = elt[0];
    let urlTail = elt[1];
    let imgUrl = elt[2];

    let card = document.createElement("div");
    card.classList.add("card");
    card.setAttribute("style", "width: 18rem; margin: 40px;");

    card.innerHTML = `
      <img class="" src="${imgUrl}" alt="${location}" width="275" height="400">
      <div class="card-body" >
          <h5 class="card-title">${location}</h5>
          <a href="info.html?key=${urlTail}&loc=${location}" class="btn btn-primary">Register</a>
      </div>
    `;

    //append to container
    tournament_cards_container.appendChild(card);

//add listener for register button
const registerButton = card.querySelector('.btn-primary');
registerButton.addEventListener("click", () => {

  const newPage = window.open("", "_blank");
  newPage.document.write(`
    <html>
      <head>
        <title>${location} Card</title>
        <style>
          body {
            font-family: Arial, sans-serif;
            background-image: linear-gradient(to right, #0072ff, #00c6ff);
            margin: 0;
            padding: 0;
          }
          header {
            background-color: #007bff;
            color: #fff;
            padding: 20px;
            text-align: center;
          }
          header a {
            text-decoration: none;

            color: #fff;
            font-weight: bold;
          }
          .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
          }
          h2 {
            margin-top: 20px;
            font-size: 24px;
          }
          img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 20px auto;
          }
          form {
            margin-top: 20px;
          }
          label {
            display: block;
            font-weight: bold;
            margin-bottom: 5px;
            color: #333;
          }
          input[type="text"],
          input[type="number"],
          select {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
          }
          select {
            height: 40px;
          }
          button[type="submit"] {
            background-color: #007bff;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
          }
          button[type="submit"]:hover {
            background-color: #0056b3;
          }
        </style>
      </head>
      <body>
        <h2>Athlete Registration</h2>
        <form method="POST" action="/registration">
          <div class="container">
            <h2>${location} Registration</h2>
            <img src="${imgUrl}" alt="${location} Image" />
            <div>
              <label for="first_name">First Name: </label>
              <input type="text" id="first_name" name="first_name" required />
            </div>
            <div>
              <label for="middle_name">Middle Name:</label>
              <input type="text" id="middle_name" name="middle_name" />
            </div>
            <div>
              <label for="last_name">Last Name:</label>
              <input type="text" id="last_name" name="last_name" required />
            </div>
            <div>
              <label for="dob">Date of Birth (YYYY-MM-DD):</label>
              <input type="text" id="dob" name="dob" required />
            </div>

            <div>
              <label>Register for:</label>
              <div>
                <label>
                  <input type="checkbox" name="registration_type" value="gi" /> Gi
                </label>
                <label>
                  <input type="checkbox" name="registration_type" value="no-gi" />
                  No-Gi
                </label>
                <label>
                  <input type="checkbox" name="registration_type" value="giAbs" />
                  Gi Absolute
                </label>
                <label>
                  <input type="checkbox" name="registration_type" value="nogiAbs" />
                  No-Gi Absolute
                </label>
              </div>
            </div>

            <!-- Gi Rank select -->
            <div id="gi_rank_div" style="display: none">
              <label for="gi_rank">Gi Rank:</label>
              <select id="gi_rank" name="gi_rank">
                {% for choice in gi_rank_choices %}
                <option value="{{ choice }}">{{ choice }}</option>
                {% endfor %}
              </select>
            </div>

            <!-- No-Gi Rank select -->
            <div id="no_gi_rank_div" style="display: none">
              <label for="no_gi_rank">No-Gi Rank:</label>
              <select id="no_gi_rank" name="no_gi_rank">
                {% for choice in no_gi_rank_choices %}
                <option value="{{ choice }}">{{ choice }}</option>
                {% endfor %}
              </select>
            </div>
            <div>
              <label for="gym">Gym:</label>
              <input type="text" id="gym" name="gym" required />
            </div>
            <div>
              <label for="weight">Weight (lbs):</label>
              <input type="number" id="weight" name="weight" required />
            </div>
            <button type="submit">Register</button>
          </div>
        </form>
      </body>
    </html>
  `);
  newPage.document.close();
});
        });
      }

  
  createTournamentCards(tournaments);

  function openNewEventForm() {
    document.getElementById('newEventModal').style.display = 'block';
  } 

  function handleNewEventSubmit(event) {
    event.preventDefault();
    let eventName = document.getElementById('eventName').value;
    let eventLocation = document.getElementById('eventLocation').value;
    tournaments.push([eventName, eventLocation, '']);
    document.getElementById('newEventModal').style.display = 'none';
  }

  document.querySelector('.text-button').addEventListener('click', openNewEventForm);
  document.getElementById('newEventForm').addEventListener('submit', handleNewEventSubmit);