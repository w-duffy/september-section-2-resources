import { useEffect, useState } from "react";
import { Image, Source } from "@unpic/react";
import "./App.css";
import {
  useLoaderData,
  createBrowserRouter,
  RouterProvider,
  redirect,
  Outlet,
  Link,
  useFetcher,
  useRouteError,
  NavLink,
  useNavigate,
} from "react-router-dom";

function Layout() {
  return (
    <>
      <nav>
      <NavLink to="/" className={({ isActive }) => isActive ? 'active' : ''}>
          Home
        </NavLink>
      </nav>
      <HomePage />
      <Outlet />
    </>
  );
}

function ImageForm() {
  let fetcher = useFetcher();
  let [isOpen, setOpen] = useState(false);

  useEffect(() => {
    if (fetcher.state === "submitting") {
      setOpen(false);
    }
  }, [fetcher.state]);

  return (
    <>
      <button onClick={() => setOpen((prev) => !prev)}>Post a new Image</button>
      {isOpen && (
        <dialog open>
          <fetcher.Form
            method="post"
            id="image-form"
            encType="multipart/form-data"
            type="file"
            action="/"
          >
            <input
              id="image"
              name="image"
              type="file"
              accept="image/*"
              required
            />
            <button style={{ pointer: "cursor" }} type="submit">
              Submit
            </button>
          </fetcher.Form>
        </dialog>
      )}
      {fetcher.state !== "idle" && <p>Submitting...</p>}
      <section>
        <Outlet />
      </section>
    </>
  );
}

function Images() {
  const { images } = useLoaderData();
  if (!images) return <p>Loading...</p>;

  return images.map((image) => (
    <Link to={`image/${image.id}`} key={image.id}>
    <div>
        <picture>
          <Source
            src={image.image}
            type="image/avif"
            width={400}
            height={300}
          />
          <Source
            src={image.image}
            type="image/webp"
            width={400}
            height={300}
          />
          <Image
            width={500}
            height={300}
            background="auto"
            src={image.image}
            alt={`Image ${image.id}`}
            loading="lazy"
          />
        </picture>
    </div>
      </Link>
  ));
}

function ImageDetail() {
  let { image } = useLoaderData();
  return (
    <Image width={500} height={300} background="auto" src={image?.image} />
  );
}

// React Router Loader
let getRoot = async () => {
  return await fetch("/api/actors/Tom"); // random actor; no utility here other than showing a loader
};

// React Router Action
let handleUpload = async ({ request }) => {
  let res = await fetch("/api/images", {
    method: "POST",
    body: await request.formData(),
  });
  if (res.status === 201) {
    throw redirect("/");
  }
  return { error: "oops" };
};


function UploadPicture (){
  // const navigate = useNavigate();
  const [image, setImage] = useState(null);
  const [imageLoading, setImageLoading] = useState(false);
  const [imageUrl, setImageUrl] = useState("");
  const handleSubmit = async (e) => {
      e.preventDefault();
      // let arr = []
      // let arr = new Array()
      console.log("Image", image)
      const formData = new FormData();
      formData.append("image", image);
      console.log("FORM DATA", formData)
      // aws uploads can be a bit slow—displaying
      // some sort of loading message is a good idea
      setImageLoading(true);
      // await dispatch(createPost(formData));
    let image = {url: "image.png"}
      const response = await fetch(`/api/images`, {
        method: "POST",
        body: JSON.stringify(image)
      });
      console.log("responose", response)
      // console.log("responose", response)
      if (response.ok) {
          const resBody  = await response.json();
          // dispatch(addPost(resPost));

          let imageObj = resBody.image
          setImageUrl(imageObj.image);
      } else {
          console.log("There was an error making your post!")
      }
      // navigate(`/images/${imageObj.id}`); ## Navigate to newly created entity
  }
  return (
    <>
    <img style={{width: "100px"}} src={imageUrl} />
    <form
        onSubmit={handleSubmit}
        encType="multipart/form-data"
        >
        <input
          type="file"
          accept="image/*"
          onChange={(e) => setImage(e.target.files[0])}
          />
        <button type="submit">Submit</button>
        {(imageLoading)&& <p>Loading...</p>}
    </form>
          </>
)
}


const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    loader: getRoot,
    action: handleUpload,
    errorElement: <ErrorBoundary />,
    children: [
      {
        path: "",
        element: <UploadPicture />,
        children: [
          {
            element: <Images />,
            index: true,
            loader: async () => await fetch("/api/images"),
          },
        ],
      },
      {
        path: "/image/:id",
        element: <ImageDetail />,
        loader: async ({ params }) => await fetch(`/api/images/${params.id}`),
      },
    ],
  },
]);




function HomePage() {
  let data = useLoaderData();
  console.log(data);
  return (
    <section>
      <h1>Hello World</h1>
      <h2>
        {data.actor?.name} is an actor in the movie {data.movies[0].title}
      </h2>
    </section>
  );
}

function ErrorBoundary() {
  const error = useRouteError();
  return (
    <div>
      <h1>Something goofed</h1>
      <p>{error.statusText || error.message}</p>
      <Link to="/">Go back Home</Link>
    </div>
  );
}

function App() {
  return <RouterProvider router={router} />;
}
export default App;
