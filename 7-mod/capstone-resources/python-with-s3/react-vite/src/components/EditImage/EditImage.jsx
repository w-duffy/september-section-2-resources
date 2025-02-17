import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { updateImage } from '../../redux/aws';
import './EditImage.css';

const EditImage = ({ image, onClose }) => {
  const dispatch = useDispatch();
  const [imageFile, setImageFile] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!imageFile) {
      setError('Please select an image');
      return;
    }

    setIsLoading(true);
    setError(null);

    const formData = new FormData();
    formData.append('image', imageFile);

    try {
      const response = await dispatch(updateImage(image.id, formData));
      if (!response.errors) {
        onClose();
      } else {
        setError(response.errors);
      }
    } catch (err) {
      setError('Failed to update image');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="edit-image-modal">
      <div className="edit-image-content">
        <h2>Edit Image</h2>
        <form onSubmit={handleSubmit}>
          <div className="current-image">
            <img src={image.image} alt="Current" className="preview" />
          </div>
          
          <div className="file-input">
            <input
              type="file"
              accept="image/*"
              onChange={(e) => setImageFile(e.target.files[0])}
            />
          </div>

          {error && <div className="error-message">{error}</div>}

          <div className="button-group">
            <button 
              type="submit" 
              className="submit-button"
              disabled={isLoading}
            >
              {isLoading ? 'Updating...' : 'Update Image'}
            </button>
            <button 
              type="button" 
              className="cancel-button"
              onClick={onClose}
              disabled={isLoading}
            >
              Cancel
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default EditImage; 