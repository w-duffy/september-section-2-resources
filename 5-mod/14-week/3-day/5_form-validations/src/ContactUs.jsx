import { useEffect } from 'react';
import { useState } from 'react';

function ContactUs() {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [phone, setPhone] = useState('');
    const [phoneType, setPhoneType] = useState('');
    const [comments, setComments] = useState('');
    const [validationErrors, setValidationErrors] = useState({});
    const [hasSubmitted, setHasSubmitted] = useState(false);

    useEffect(() => {
        const errors = {};

        if (name.length <= 0) {
            errors.name = 'Please enter your Name';
        }

        if (!email.includes('@')) {
            errors.email = 'Please provide a valid Email';
        }

        if (!phone.length) {
            errors.phone = 'Please gimme yo numba';
        }

        setValidationErrors(errors);
    }, [name, email, phone]);



    const onSubmit = (e) => {
        // Prevent the default form behavior so the page doesn't reload.
        e.preventDefault();

        setHasSubmitted(true);

        const myErrors = Object.values(validationErrors);

        if (myErrors.length) {
            // alert(`The following errors were found: \n${myErrors.join('\n')}`);
            return;
        }

        // Create a new object for the contact information.
        const contactUsInformation = {
            name,
            email,
            phone,
            phoneType,
            comments,
            submittedOn: new Date(),
        };

        // Ideally, you'd persist this information to a database using a RESTful API.
        // For now, though, just log the contact information to the console.
        console.log(contactUsInformation); //! Submission point

        setHasSubmitted(false);

        // Reset the form state.
        setName('');
        setEmail('');
        setPhone('');
        setPhoneType('');
        setComments('');
    };

    return (
        <div>
            <h2>Contact Us</h2>
            <form onSubmit={onSubmit}>
                <div>
                    <label htmlFor="name">Name:</label>
                    <input
                        id="name"
                        type="text"
                        required
                        onChange={(e) => setName(e.target.value)}
                        value={name}
                    />
                    {hasSubmitted && validationErrors.name && (
                        <div className="error">{`* ${validationErrors.name}`}</div>
                    )}
                </div>
                <div>
                    <label htmlFor="email">Email:</label>
                    <input
                        id="email"
                        type="text"
                        onChange={(e) => setEmail(e.target.value)}
                        value={email}
                    />
                    <div className="error">
                        {hasSubmitted &&
                            validationErrors.email &&
                            `* ${validationErrors.email}`}
                    </div>
                </div>
                <div>
                    <label htmlFor="phone">Phone:</label>
                    <input
                        id="phone"
                        type="text"
                        onChange={(e) => setPhone(e.target.value)}
                        value={phone}
                    />
                    {hasSubmitted && validationErrors.phone && (
                        <div className="error">{`* ${validationErrors.phone}`}</div>
                    )}
                    <select
                        name="phoneType"
                        onChange={(e) => setPhoneType(e.target.value)}
                        value={phoneType}
                    >
                        <option value="" disabled>
                            Select a phone type...
                        </option>
                        <option>Home</option>
                        <option>Work</option>
                        <option>Mobile</option>
                    </select>
                </div>
                <div>
                    <label htmlFor="comments">Comments:</label>
                    <textarea
                        id="comments"
                        name="comments"
                        onChange={(e) => setComments(e.target.value)}
                        value={comments}
                    />
                </div>
                <button>Submit</button>
            </form>
        </div>
    );
}

export default ContactUs;
