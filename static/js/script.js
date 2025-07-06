document.getElementById('preferenceForm').addEventListener('submit', async function (e) {
    e.preventDefault();
  
    const amenities = document.getElementById('amenities').value.split(',').map(a => a.trim());
    const minSafetyRating = document.getElementById('minSafetyRating').value;
    const maxCostOfLiving = document.getElementById('maxCostOfLiving').value;
  
    const response = await fetch('/api/match', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        amenities: amenities,
        min_safety_rating: minSafetyRating,
        max_cost_of_living: maxCostOfLiving
      })
    });
  
    const data = await response.json();
    displayResults(data);
  });
  
  function displayResults(neighborhoods) {
    const list = document.getElementById('neighborhoodList');
    list.innerHTML = '';
    if (neighborhoods.length > 0) {
      neighborhoods.forEach(n => {
        const li = document.createElement('li');
        li.textContent = n.name;
        list.appendChild(li);
      });
    } else {
      list.innerHTML = '<li>No neighborhoods matched your criteria.</li>';
    }
  }
  