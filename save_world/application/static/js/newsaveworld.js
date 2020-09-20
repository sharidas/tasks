/*function addNewSaviour(dtime, howsaved, thanks_to_people) {
    console.log("Hello");
    console.log("dtime = ", dtime, " howsaved = ", howsaved, " thanks = ", thanks_to_people);
    let data = {
        "dtime": dtime,
        "howsaved": howsaved,
        "thanks_to_people": thanks_to_people
    };

    console.log("Json data = ", JSON.stringify(data));

    return JSON.stringify(data);
    //return false;
}*/

(function () {
    let newsaviourid = document.getElementById('new-saviour-data');
    newsaviourid.onsubmit = async (e) => {
        e.preventDefault();

        inputData = newsaviourid.getElementsByTagName('input');
        textData = newsaviourid.getElementsByTagName('textarea')

        if ( inputData.length > 0 && textData.length > 0) {

            let requestData = {
                'dtime': inputData[0].value,
                'howsaved': inputData[1].value,
                'thanks_to_people': textData[0].value,
                'key': 'LETS_SAVE_WORLD_123456',
            };

            let response = await fetch('/save/world/', {
                method: 'POST',
                mode: 'cors',
                redirect: 'follow',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(requestData),
            }).then(data => {
                window.location = "/save/world/";
            });
        }
    };
})();