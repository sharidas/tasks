(function() {
    let textElements = document.querySelectorAll(".changable");

    textElements.forEach(element => {
        element.addEventListener("input", function (e) {
            console.log(e.target.value)
            element.textContent = e.target.value
            let submitBtn = element.parentNode.parentNode.lastElementChild;
            submitBtn.firstChild.disabled = false
        });

        /**
         * Now the submit button is enabled. So if the user clicks the submit
         * button we may disable it.
         */
        let submitBtn = element.parentNode.parentNode.lastElementChild;
        submitBtn.firstChild.addEventListener("click", function (submitEvent) {
        /**
         * We need to get the data of the row to submit!!!
         */
            let howSaved = element.parentNode.parentElement.getElementsByClassName("how-saved")[0].textContent
            let thankfuPeople = element.textContent
 
            updateData("/save/world/", {"howsaved": howSaved, "thanks_to_people": thankfuPeople, "key": "LETS_SAVE_WORLD_123456"})
                .then(data => {
                    console.log(data);
                })
                .catch(error => {
                    console.error('Error: ', console.error());
                });
             });
    });

    async function updateData(url = "", data = {}) {
        const response = await fetch(url, {
            method: 'PUT',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
              },
              body: JSON.stringify(data)
        });
        return response.json();
    }

    let nextPageElement = document.getElementById('next-page');
    
    nextPageElement.addEventListener('click', function () {
        let hrefData = window.location.href.split("=");
        if (hrefData.length === 2){
            hrefData[1] = (parseInt(hrefData[1]) + 1).toString();
            window.location.href = hrefData.join('=');
        } else {
            window.location.href = '/save/world/?page=2';
        }
    });

    let prevPageElement = document.getElementById('previous-page');

    prevPageElement.addEventListener('click', function () {
        let hrefData = window.location.href.split("=");
        if (hrefData.length === 2){
            if ((parseInt(hrefData[1]) - 1) >= 2) {
                hrefData[1] = (parseInt(hrefData[1]) - 1).toString();
                window.location.href = hrefData.join('=');
            } else {
                window.location.href = '/save/world/?page=1';
            }
        }
    });
})();
