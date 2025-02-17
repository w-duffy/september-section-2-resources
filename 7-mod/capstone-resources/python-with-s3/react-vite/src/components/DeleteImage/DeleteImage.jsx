import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { deleteImage } from '../../redux/aws';
import './DeleteImage.css';

const DeleteImage = ({ image, onClose }) => {
  const dispatch = useDispatch();
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleDelete = async () => {
    setIsLoading(true);
    setError(null);

    try {
      const response = await dispatch(deleteImage(image.id));
      if (response.success) {
        onClose();
      } else {
        setError(response.message || 'Failed to delete image');
      }
    } catch (err) {
      setError('Failed to delete image');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="delete-image-modal">
      <div className="delete-image-content">
        <h2>Delete Image</h2>
        <p>Are you sure you want to delete this image? This action cannot be undone.</p>
        
        <div className="image-preview">
          <img src={image.image} alt="To be deleted" />
        </div>

        {error && <div className="error-message">{error}</div>}

        <div className="button-group">
          <button 
            className="confirm-button"
            onClick={handleDelete}
            disabled={isLoading}
          >
            {isLoading ? 'Deleting...' : 'Delete Image'}
          </button>
          <button 
            className="cancel-button"
            onClick={onClose}
            disabled={isLoading}
          >
            Cancel
          </button>
        </div>
      </div>
    </div>
  );
};

export default DeleteImage; 