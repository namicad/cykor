# 주소
http://namicad.pythonanywhere.com/ 
# list
첫 화면으로 글 목록이 뜨고 제목, 작성자, 내용 순으로 글이 작성되어 있다. 내용을 누르면 해당 글 화면으로 넘어가고, 오른쪽 아래에는 글을 작성하는 버튼이 존재한다. 로그인을 하지 않으면 로그인 화면으로 넘어간다.

윗줄에는 목록으로 넘어가는 버튼과 로그인 버튼이 존재한다. 로그인한 상태였다면, 로그인 버튼 대신 로그아웃 버튼이 생기고 hello,{{id}}!가 뜬다.

# post_form
글 작성화면으로 넘어오면 제목과 내용을 적는 칸이 있고 submit 버튼을 누르면, 내용은 저장되고 글 목록으로 넘어간다.

# post_detail
글 목록에서 내용을 누르면 넘어올 수 있다. 글을 수정할 수 없지만, 아래에 edit 버튼을 누르면 수정가능하도록 변경된다. delete 버튼을 누르면 글이 삭제된다. 작성자가 아니라면 불가능하다. 
