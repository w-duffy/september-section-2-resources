import { useParams, useNavigate } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { getImageById } from "../redux/aws";
import { useEffect, useState } from "react";
import EditImage from "./EditImage/EditImage";
import DeleteImage from "./DeleteImage/DeleteImage";
import "./ImageDetail.css";

export default function ImageDetail() {
  let { id } = useParams();
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const loadedImage = useSelector((state) => state.images.allImages[id]);
  const noImageError = useSelector((state) => state.images.error);
  const [showEditModal, setShowEditModal] = useState(false);
  const [showDeleteModal, setShowDeleteModal] = useState(false);

  useEffect(() => {
    dispatch(getImageById(id));
    return () => {
      dispatch({ type: "error/cleanup" });
    };
  }, [dispatch, id]);

  const handleEditClose = () => {
    setShowEditModal(false);
  };

  const handleDeleteClose = () => {
    setShowDeleteModal(false);
    navigate("/"); 
  };

  if (noImageError.message) return <p>{noImageError.message}</p>;

  if (!loadedImage) return <p>Loading Spinner...</p>;


  return (
    <div className="image-detail-container">
      <div className="image-wrapper">
        <img src={loadedImage.image} alt="Detailed view" />
      </div>

      <div className="image-actions">
        <button
          className="edit-button"
          onClick={() => setShowEditModal(true)}
        >
          Edit Image
        </button>
        <button
          className="delete-button"
          onClick={() => setShowDeleteModal(true)}
        >
          Delete Image
        </button>
      </div>

      {showEditModal && (
        <EditImage
          image={loadedImage}
          onClose={handleEditClose}
        />
      )}

      {showDeleteModal && (
        <DeleteImage
          image={loadedImage}
          onClose={handleDeleteClose}
        />
      )}
    </div>
  );
}
