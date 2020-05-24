Topic Modeling on Bills of the US Congress
===========================
Contributors
--------
Eva Gmelich Meijling, Rajiv Manichand and Hanabi Ono

Abstract
--------

This project generates and applies an LDAtopic model on Bills of the US Congressin the period between 1973 until present.The topics are analysed in attempt to iden-tify which topics are of particular interestto  either  the  Democratic  or  Republicanparty. 

Research questions
------------------

What main trends can we distinguish between the two US parties, democrats and republicans, based upon changes in legislation (bills and amendments) in the US congress? 

-   Which bill topics are focussed on during what times?

-   How are the votes distributed on the bill?

-   Do they get more polarized?

-   What topics are important to the president (regarding the State of the Union)?

-   What are the ideologies of both parties?



Dataset
-------

Dataset 1:  Public domain code that collects data about the bills, amendments, roll call votes, and other core data about the U.S. Congress.

-   The repository is a scraper that retrieves congress data from Internet sources, however data from 1973-now is also available as files. For this reason, we initially only use data from this timeframe
-   The repository contains very clear information on how to manage and process the data. We will enrich the data by assigning each bill to a topic and the dominant party in congress.
-   For each bill, a JSON file is given with all relevant information, such as titles, description and statusses.

Examples:\
Size and format: The size of the data set is huge since it contains bills from 1790 - 2014 and also other information. The format is a GitHub repository.\
Link: <https://github.com/unitedstates/congress/>



A tentative list of milestones for the project
----------------------------------------------

Week 11:\
Go through the data sets and find out the best way we can extract the data from them.

Week 12:\
Clean up data sets so we can use them.

Week 13:\
Have every bill assigned a topic and find out the ideology of the congress during that time.

Week 14:\
Report on the relation between topics of the bills and the congress.

Week 15:\
Compare the report to the second dataset, where the white house (president) presents for him the most important topics.

Week 16:\
Finalize project

Documentation
-------------

This can be added as the project unfolds. You should describe, in particular, what your repo contains and how to reproduce your results.


Miscellaneous
-------------
Simlar paper:  Lexical shifts, substantive changes, and continuity in State of the Union discourse, 1790--2014
Link: <https://www.pnas.org/content/pnas/112/35/10837.full.pdf>
