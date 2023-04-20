## Parameter Optimization of SVM:
A mathematical model in Machine Learning is designed with a set of parameters that require learning from the data. However, there exist certain parameters known as Hyperparameters which cannot be directly learned from the data. These Hyperparameters are generally selected by humans based on prior knowledge or trial-and-error methods before commencing the training process. In the case of SVM, certain Hyperparameters such as the choice of C or gamma values are crucial for optimal performance, but their determination is a challenging task. Nevertheless, the optimal Hyperparameters can be found by exhaustively trying out all combinations and selecting the ones that yield the best results.

## Dataset:
#### [LINK](https://archive.ics.uci.edu/ml/datasets/Shill+Bidding+Dataset)
#### Shill Bidding Dataset:
![image](https://user-images.githubusercontent.com/91868707/233176760-aae0b44e-b3d1-4e41-9cba-967aff35843c.png)

#### Attributes used:

* Bidder Tendency: A shill bidder participates exclusively in auctions of few sellers rather than a diversified lot. This is a collusive act involving the fraudulent seller and an accomplice.
* Bidding Ratio: A shill bidder participates more frequently to raise the auction price and attract higher bids from legitimate participants.
* Successive Outbidding: A shill bidder successively outbids himself even though he is the current winner to increase the price gradually with small consecutive increments.
* Last Bidding: A shill bidder becomes inactive at the last stage of the auction (more than 90\% of the auction duration) to avoid winning the auction.
* Auction Bids: Auctions with SB activities tend to have a much higher number of bids than the average of bids in concurrent auctions.
* Auction Starting Price: a shill bidder usually offers a small starting price to attract legitimate bidders into the auction.
* Early Bidding: A shill bidder tends to bid pretty early in the auction (less than 25\% of the auction duration) to get the attention of auction users.
* Winning Ratio: A shill bidder competes in many auctions but hardly wins any auctions.
* Auction Duration: How long an auction lasted.

## Methodology:
Divide the dataset into 70-30 for training and testing with 10 different samples. Optimize the SVM for every sample with mutiple iterations and report the best parameters.

* Comparative performance of Optimized-SVM with different samples:

![Screenshot (86)](https://user-images.githubusercontent.com/91868707/233196652-83530917-f31d-4bca-8070-9d35fc7ef7d8.png)

* The following Convergence graph shows the accuracy of sample 4 (maximum accuracy) over the 1000 iterations:

![image](https://user-images.githubusercontent.com/91868707/233446888-5ff95e60-f039-4878-b1da-d9db90a51132.png)
