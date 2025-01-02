import { useState } from 'react';

export default function ContactUs() {
    console.log('Just rerendered');

    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [phone, setPhone] = useState('');
    const [phoneType, setPhoneType] = useState('');
    const [comments, setComments] = useState('');
    // const [isSubmitted, setIsSubmitted] = useState(false);

    // useEffect(() => {
    //     const sendFetch = async () => {
    //         const contactUsInformation = {
    //             name,
    //             email,
    //             phone,
    //             phoneType,
    //             comments,
    //             submittedOn: new Date(),
    //         };
    //         await fetch('/api/spots', 'POST');

    //         setName('');
    //         setEmail('');
    //         setPhone('');
    //         setPhoneType('');
    //         setComments('');
    //         setIsSubmitted(false);
    //     };

    //     if (isSubmitted) sendFetch();
    // }, [isSubmitted]);

    const handleSubmit = (e) => {
        e.preventDefault();

        const contactUsInformation = {
            name,
            email,
            phone,
            phoneType,
            comments,
            submittedOn: new Date(),
        };

        console.log('Submitting...', contactUsInformation);

        setName('');
        setEmail('');
        setPhone('');
        setPhoneType('');
        setComments('');

        // setIsSubmitted(true);
    };

    return (
        <div>
            <h2>Contact Us</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="name">Name:</label>
                    <input
                        id="name"
                        type="text"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                    />
                </div>
                <div>
                    <label htmlFor="email">Email:</label>
                    <input
                        id="email"
                        type="text"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                    />
                </div>
                <div>
                    <label htmlFor="phone">Phone:</label>
                    <input
                        id="phone"
                        type="text"
                        value={phone}
                        onChange={(e) => setPhone(e.target.value)}
                    />
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
