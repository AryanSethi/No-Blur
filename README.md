<h1 align="center">Image DeBlurring AutoEncoder Network</h1><br/>

<h2>Overview</h2>
<div>
  <img src="https://github.com/AryanSethi/Deblurring_autoencoder/blob/master/assets/blur.gif" width= "300" height= "250" align = "right" alt="BLURRY"/>
  In many real world applications, sometimes there is a need to zoom a specific area of 
  interest in the image without the loss of quality i.e having a high resolution image, 
  e.g. in surveillance and  space imaging applications.
  <br/>
  Having high resolution imaging setups is not always possible so me, [Misanthropic][2] and my Computer Vision Professor Dr Shailendra Tiwari are 
  experimenting with Autoencoders to make a low computation Super-resolution model. We are using the famous [UNet][1] architecture (brilliant piece of work by the way) as our 
  base to deblur the images. The network basically extracts the important features of the image while reducing its spacial features and then Up-Sampling those compact features 
  aka recreating the original sized image but de-blurred. 
</div>

<h2>Research</h2>
<div>
  It's been some time now that we've been working on the subject. As we went through the project, we kept recording all kinds of logs like hyper-parameters and their      
  corresponding results. We've managed to attain some good quality results(at very low computation costs) that can be improved drastically if given proper attention by experts 
  in the field. We're planning to publish the work we've done so far and see where it takes us :D 
</div>

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














[1]: https://arxiv.org/abs/1505.04597  "Unet Paper Link"
[2]: https://github.com/MisanthropicDeity "Vidhu Shikhar Joshi"
