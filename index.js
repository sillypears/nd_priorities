$(function() {
    $.getJSON('necrodancer.json', function(data) {
        var content = `<table id="enemies" class="table table-bordered">`;
        const width = $(document).width()
        const total = data.length
        const rows =  Math.floor(width/total)+1
        data.forEach(function(e, i) {
            if ((i%rows) === 0 ||  i === 0) {
                content += `<tr>`;
            }
            let ttip = `Name: ${e.name} <br />Type: ${e.type} <br />Priority: ${e.priority}`;
            content += `<td class="text-center"> ${e.priority}<img data-html="true" data-toggle="tooltip" title="${ttip}" src="${e.sprite}"></td>`
            if ( (i+1%rows) === 0 && i !== 0) {
                content += `</tr>`;
            }
        });
       content += `</tr></table>`;
       $('div#content').html(content);
       $('[data-toggle="tooltip"]').tooltip();
    });
});