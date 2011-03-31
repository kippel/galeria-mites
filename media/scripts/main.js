  var first = true;
  last_search = '';
  function search(e){
    if (first){
      var text_search = $('#tx-search-main').val();
    }else{
      var text_search = $('#tx-search-header').val();
    }
    
    if (last_search == text_search || text_search == ''){
    
        return false;
    }
    last_search = text_search;
    
    $.post('/load', {search : text_search}, function( data){
      
      if (data.num==0){
        $('#galeria').html('');
        $('#not_found').show();
      }else{
        $('#not_found').hide();
        if (first){
          first = false;
          $('#div-search').hide('slow');
          $('#tx-search-header').val( text_search );
          $('#div-search-header').show();
          $('#tx-search-header').focus();
        }
        
        $('#galeria').html(data.html);
      }
    },'json');
  }

 
  $(document).ready( function(){
            
            $('#bt-search-main').click( search );
            $('#tx-search-header').keypress(function(e){
              if (e.keyCode == 13){
                search();
              }
              
            
            });
  });