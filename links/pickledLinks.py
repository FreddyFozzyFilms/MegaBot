import setup
import pickle




# pickle dump the list object

    # default protocol is zero
    # -1 gives highest prototcol and smallest data file size


# pickle load the list object back in (senses protocol)

 
mylist = [
'Frank',
'Paul',
'Mary']

fname = "list101.pkl"
# pickle dump the list object
with open(fname, "wb") as fout:
    # default protocol is zero
    # -1 gives highest prototcol and smallest data file size
    pickle.dump(mylist, fout, protocol=-1)

# pickle load the list object back in (senses protocol)
with open(fname, "rb") as fin:
    mylist2 = pickle.load(fin)

# visual compare
@setup.client.command
async def alink(ctx, *, question):


  ctx.send(f'Question: {question}\nAnswer: {setup.random.choice(mylist)}')
