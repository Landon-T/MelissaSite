document.addEventListener('DOMContentLoaded', function() {

    fetch('/edit/pages', {
        method: 'PUT',
        body: JSON.stringify({
            
        })
      })
      .then(response => response)
      .then(result => {
        console.log(result);
   
      })
      .catch(error => {
        alert(error);
      });
});