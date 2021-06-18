<h1 align="center">Image DeBlurring AutoEncoder Network</h1><br/>

<h2>Overview</h2>
  <img src="https://github.com/AryanSethi/Deblurring_autoencoder/blob/master/assets/blur.gif" width= "300" height= "250" align = "right" alt="BLURRY"/>
In our day to day lives, we take a lot of pictures on our phones everyday. But so many times, they are not of a quality good enough. A shaky hand and the 
image blurs like taken on a 2 mega Pixel camera. Images being blur is a very common thing and we don't really have any effective way of de-blurring them.
  <br/>
  So, [Vidhu Joshi][2] and I experimented for weeks to make a Neural netowrk that could even remote address this issue. We used the famous [UNet][1] architecture (brilliant piece of work by the way) as our 
  base netowrk to deblur the images. The network basically extracts the important features of the image while reducing its spacial features and then Up-Sampling those compact features 
  aka recreating the original sized image but de-blurred.  


<h2>Research</h2>
<div>
  It's been some time now that we've been working on the subject. As we went through the project, we kept recording all kinds of logs like hyper-parameters and their      
  corresponding results. We've managed to attain some good quality results(at very low computation costs) that can be improved drastically if given more attention. 
    We're planning to publish the work we've done so far and see where it takes us :D

<b>If anyone sees this of any interest for further research, please reach out to us anytime.</b>
</div>

<h2>Directory Structure</h2>
We've tried to keep the directory structure and codebase as clean as possible. The utils directory contains a number of scripts written to 
setup the entire project, like keras custom image generator classes, scripts to make the deblurred dataset, renaming files,etc

As we go along trying new stuff in new python notebooks, we keep adding them to the `model_exps` directory and name them `try1` , `try2` and so o.
At the top of each notebook is marked down specific parameters that were used in that particular experiment (eg. Epochs, depth of netowrk,
loss functions,etc) as well as the results fetched (eg. loss value). The `data` direcotry has not been uploaded due to our personal
reasons but its structure is as follows:

<img src="https://github.com/AryanSethi/Deblurring_autoencoder/blob/master/assets/data_struct.png" height="200"/>

The `best_models` directory contains the all the saved models (in keras Saved Model format) that fetched results which were interested in
any way.


<h2>Training</h2>

<img src="https://github.com/AryanSethi/Deblurring_autoencoder/blob/master/assets/platform.png" height = "200"/>

<h2>Some results</h2>
<div>
  <ul>
    <li><strong>First Image -</strong> Blurred</li>
    <li><strong>Second Image -</strong> Clear</li>
    <li><strong>Third Image -</strong> Predicted Clear</li>
  </ul>
  <img src="https://github.com/AryanSethi/Deblurring_autoencoder/blob/master/assets/try4d-18-6.jpg" width="500" height="166"/>
  <br/>
  <img src="https://github.com/AryanSethi/Deblurring_autoencoder/blob/master/assets/try4d-32-0.jpg" width="500" height="166"/>
</div>














[1]:https://arxiv.org/abs/1505.04597  "Unet Paper Link"
[2]:https://github.com/MisanthropicDeity "Vidhu Shikhar Joshi"
