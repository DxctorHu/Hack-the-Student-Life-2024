document.addEventListener('DOMContentLoaded', function() {
    console.log("received click");
    fetch('https://o2t5amundyl2sw2s5333trznq40gevcf.lambda-url.us-west-2.on.aws/')
      .then(response => response.json())
      .then(data => {
        displayData(data);
        // Process and display data in your popup here
      })
      .catch(error => {
        console.error('Error:', error);
      });
  });

function displayData(data) {
    const sidebar = document.getElementById('sidebar');
    data.forEach(item => {
        const itemElement = document.createElement('div');
        itemElement.className = 'item';
    
        for (const key in item) {
          const div = document.createElement('div');
          const spanKey = document.createElement('span');
          spanKey.className = 'key';
          spanKey.textContent = `${key}: `;
          const spanValue = document.createElement('span');
          spanValue.textContent = item[key];
    
          div.appendChild(spanKey);
          div.appendChild(spanValue);
          itemElement.appendChild(div);
        }
    
        sidebar.appendChild(itemElement);
      });
}