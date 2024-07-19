const submit = document.querySelector('.btn');

submit.addEventListener('click', async function(e) {
    const searchString = document.getElementById("searchString").value;
    const searchField = document.getElementById("searchField").value;
    const maxResult = document.getElementById("maxResults").value

    const formData = new FormData();
    formData.append("search_string", searchString)
    formData.append("search_field", searchField);
    formData.append("max_result", maxResult);
    
    const requestOptions = {
        headers: {
            "Content-Type":"text"
        },
        mode: "no-cors",
        method: "POST",
        body: formData,
    };
    
    const response = await fetch(window.location.href + "api/recall", requestOptions)
    .then(res => {
        return res.blob().then((data) => {
            return {
                data: data,
                //filename: res.headers.get('Content-disposition').split('filename=')[1],
            };
        });
    })
    .then(({data, filename}) => {
        //const filename = headers.get("content-disposition").split('filename=')[1];
        var a = document.createElement("a");
        a.href = window.URL.createObjectURL(data);
        a.download = filename;
        a.click(); 
    }); 
});
