import { useDispatch, useSelector } from "react-redux";
import { useLoaderData, Link } from "react-router-dom";
import { useEffect, useState, useRef } from "react";
import { Image } from "@unpic/react";
import { selectImages, createImage, getAllImages } from "../redux/aws";

function ImageCard({ image }) {
  if(image.image.endsWith("mp4")) {
        return (
      <video
        src={image.image}
        autoPlay={true}
        controls
        style={{
          width: '500px',
          height: '300px',
          objectFit: 'cover',
          borderRadius: '8px',
          margin: '10px 0'
        }}
      />
    );

  }
  return (
    <Link to={`/image/${image.id}`}>
      <picture>
        <Image
          width={500}
          height={300}
          background="auto"
          src={image.image}
          alt={`Image ${image.id}`}
          loading="lazy"
        />
      </picture>
    </Link>
  );
}

const AllImagesLandingPage = () => {
  const dispatch = useDispatch();
  const images = useSelector(selectImages);

  useEffect(() => {
    dispatch(getAllImages());
  }, [dispatch]);

  if (!images) return <p>No images yet, add one below!</p>;

  return (
    <section style={{
      padding: '2rem',
      maxWidth: '1200px',
      margin: '0 auto'
    }}>
      <h2 style={{
        fontSize: '2rem',
        color: '#333',
        marginBottom: '2rem',
        textAlign: 'center'
      }}>Image Gallery</h2>
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(500px, 1fr))',
        gap: '2rem',
        justifyItems: 'center'
      }}>
        {images.map((image) => (
          <div key={image.id} style={{
            boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
            borderRadius: '8px',
            overflow: 'hidden',
            transition: 'transform 0.2s ease-in-out',
            ':hover': {
              transform: 'scale(1.02)'
            }
          }}>
            <ImageCard image={image} />
          </div>
        ))}
      </div>
    </section>
  );
};

// const AllImagesLandingPage = () => {
//   const dispatch = useDispatch();
//   const images = useSelector(selectImages);

//   useEffect(() => {
//     dispatch(getAllImages());
//   }, [dispatch]);

//   if (!images) return <p>No images yet, add one below!</p>;
//   console.log(images);

//   return (
//     <section>
//       <h2>Image Gallery</h2>
//       {images.map((image) => (
//         <ImageCard key={image.id} image={image} />
//       ))}
//     </section>
//   );
// };

import './UploadPicture.css';

const UploadPicture = () => {
  const dispatch = useDispatch();
  const user = useSelector((state) => state.session.user);
  const isAddingNewImage = useSelector((state) => state.images.loading);
  const fileInputRef = useRef(null);
  const [userUpload, setUserUpload] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!userUpload) return; // Prevent submission if no file is selected
    const formData = new FormData();
    formData.append("image", userUpload);
    dispatch(createImage(formData));
    fileInputRef.current.value = "";
    setUserUpload(null);
  };

  if (!user) return <p className="upload-message">Please log in to upload images</p>;

  return (
    <section className="upload-section">
      <h2 className="upload-title">{isAddingNewImage ? "Uploading..." : "Upload an Image"}</h2>
      <form className="upload-form" onSubmit={handleSubmit} encType="multipart/form-data">
        <div className="form-group">
          <label htmlFor="image-upload" className="form-label">Select Image:</label>
          <input
            id="image-upload"
            type="file"
            accept="image/*"
            onChange={(e) => setUserUpload(e.target.files[0])}
            ref={fileInputRef}
            className="form-input"
            required
          />
        </div>
        <button type="submit" className="upload-button" disabled={isAddingNewImage}>
          {isAddingNewImage ? "Uploading..." : "Upload Image"}
        </button>
      </form>
    </section>
  );
};


// const UploadPicture = () => {
//   const dispatch = useDispatch();
//   const user = useSelector((state) => state.session.user);
//   const isAddingNewImage = useSelector((state) => state.images.loading);
//   const fileInputRef = useRef(null);
//   const [userUpload, setUserUpload] = useState(null);

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     const formData = new FormData();
//     formData.append("image", userUpload);
//     dispatch(createImage(formData));
//     fileInputRef.current.value = "";
//     setUserUpload(null);
//   };

//   if (!user) return <p>Please log in to upload images</p>;

//   return (
//     <section>
//       <h2>{isAddingNewImage ? "Uploading..." : "Upload an Image"}</h2>
//       <form onSubmit={handleSubmit} encType="multipart/form-data">
//         <input
//           type="file"
//           accept="image/*"
//           onChange={(e) => setUserUpload(e.target.files[0])}
//           ref={fileInputRef}
//         />
//         <button type="submit">Upload Image</button>
//       </form>
//     </section>
//   );
// };

export default function AWS() {
  return (
    <main>
      <AllImagesLandingPage />
      <UploadPicture />
    </main>
  );
}

// This is just showing how to use useLoaderData from react router
export function Images() {
  const { images } = useLoaderData();

  if (!images.length) return <p>No images yet, click Home to add one...</p>;

  return images.map((image) => (
    <picture key={image.id}>
      <Image
        width={500}
        height={300}
        background="auto"
        src={image.image}
        alt={`Image ${image.id}`}
        loading="lazy"
      />
    </picture>
  ));
}
