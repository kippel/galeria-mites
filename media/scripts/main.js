
  $(document).ready( function(){
            
            $('#bt-search-main').click( function(e){
              
                  $.post('/load', {search : $('#tx-search-main').val()}, function( data){
                    if (data.num==0){
                      $('#galeria').html('');
                      $('#not_found').show();
                    }else{
                      $('#not_found').hide();
                      $('#galeria').html(data.html);
                    }
                  },'json');
            });
  });