$(document).ready(function(){
   $('.reqbtn').click(function () {
   var id;
   var item=$(this);
   console.log('hello');
   id=$(this).attr('data-id');
   $.get('/home/sendreq',{id:id},function (data,status) {
       item.html(data);
   })
});
      $('.accbtn').click(function () {
   var id;
   var item=$(this);
   console.log('hello');
   id=$(this).attr('data-id');
   $.get('/home/accreq',{id:id},function (data,status) {
       item.html(data);
   })
});
});