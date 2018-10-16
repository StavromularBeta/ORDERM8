from createtb import CreateTb
from dbviews import DbViews

NewCreate = CreateTb()
NewCreate.create_table(1)
NewCreate.create_table(2)
NewCreate.create_table(3)
NewCreate.create_table(4)
NewCreate.create_table(5)

NewView = DbViews()
for item in NewView.master_table_query():
    print item
