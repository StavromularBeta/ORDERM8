from createtb import CreateTb
from dbviews import DbViews
from addel import AdDel

NewCreate = CreateTb()
NewCreate.create_table(1)
NewCreate.create_table(2)
NewCreate.create_table(3)
NewCreate.create_table(4)
NewCreate.create_table(5)

NewDelete = AdDel()
NewDelete.delete_table(1)

NewView = DbViews()
for item in NewView.master_table_query():
    print item[1]
