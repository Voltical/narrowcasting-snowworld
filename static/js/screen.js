console.log("screen.js geladen");
document.getElementById("lockers").innerText = data.lockers_available;
document.getElementById("parking").innerText = data.parking_free;
document.getElementById("piste-temp").innerText = data.piste_temp + "°C";
document.getElementById("outdoor-temp").innerText = data.outdoor_temp + "°C";

async function loadStats() {
  const res = await fetch("/api/stats");
  const data = await res.json();

  if (!data) {
    console.warn("Geen stats data");
    return;
  }

  document.getElementById("lockers").innerText = data.lockers_available;

  document.getElementById("parking").innerText = data.parking_free;

  document.getElementById("piste-temp").innerText = data.piste_temp + "°C";

  document.getElementById("outdoor-temp").innerText = data.outdoor_temp + "°C";
}

loadStats();
