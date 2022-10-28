The code should be able to do following things

        1) we should be able to add a template easily for a task
        2) We should be able to add a task

### Step 1 Add a template for a given task

Add template information in ``template/rte_prompts.csv`` 

### Step 2 Use this csv to create prompts

\todo 
 - samples are from training set of rte?
 - How to select 4 examples? Choose index as webson. these 4 will remain same for all test samples
 - evaluation is on test set of rte

Finally what we want is columns like this in the result section

Task -rte
Prompt | GPT3 accuracy | OPT accuracy

Task -mnli
Prompt | GPT3 accuracy | OPT accuracy





template 
            --> prompt --> model
4 examples
(this depend on random seed)

1 query
(run on all query from validation set)


1 template -  {premise} Are we justified in saying that "{hypothesis}"?

val set - size 20 - 20 queries

10 templates - 200 queries

val performance - 

-------------------

1 template -> 20 queries -> 1 accuracy

10 accuracy -> box plot, mean , median, std dev, 



--------------------------------------------

1) csv file to store the template like webson did (1 csv for one task (rte, mnli))

2) processing input

2) function to read this csv file and use