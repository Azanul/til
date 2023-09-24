```js
async function downloadAndZipImages(images) {
  const zip = new JSZip();
  const promises = [];

  images.forEach((image, index) => {
    const imageUrl = image.src;
    const imageFilename = `image_${index + 1}.jpg`;

    promises.push(
      fetch(imageUrl)
        .then(async (response) => {
          if (!response.ok) {
            console.warn(`Image ${imageFilename} was blocked by client. Skipping.`);
            return;
          }

          const blob = await response.blob();
          zip.file(imageFilename, blob);
        })
        .catch((error) => {
          console.error(`Error fetching image ${imageFilename}:`, error);
        })
    );
  });

  await Promise.all(promises);

  const content = await zip.generateAsync({ type: 'blob' });
  const zipBlob = new Blob([content]);

  saveAs(zipBlob, 'images.zip');
}

const images = document.querySelectorAll('img');

downloadAndZipImages(images);
```
