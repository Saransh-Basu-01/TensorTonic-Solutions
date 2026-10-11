## The Problem: Rotation and Translation Don't Mix Easily

When working with 3D points, two of the most common operations are **rotation** (spinning an object around some axis) and **translation** (sliding an object from one position to another).

Rotation is a *linear* operation. If you have a 3x3 rotation matrix $R$ and a point $p$, you can rotate the point by computing:

$$
p' = R \cdot p
$$

Translation, on the other hand, is an *affine* operation. You add a vector $t$ to shift the point:

$$
p' = p + t
$$

If you want to do both at once, you would write:

$$
p' = R \cdot p + t
$$

This works, but it is awkward. You cannot represent "rotate then translate" as a single matrix multiplication in 3D. This means you cannot chain multiple rotation-and-translation steps together using standard matrix multiplication. Every step requires a separate multiply and a separate addition. This becomes painful fast, especially in robotics or graphics where you might have dozens of coordinate frames chained together.

**Homogeneous coordinates** solve this by lifting everything into 4D, so that rotation and translation both become matrix multiplications.

---

## What Are Homogeneous Coordinates?

The core idea is simple: take a 3D point $(x, y, z)$ and append a 1 at the end to get a 4D vector:

$$
p_h = \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix}
$$

This extra coordinate (often called the $w$-coordinate) is what makes the trick work. By operating in this 4D space, we can encode both rotation and translation inside a single $4 \times 4$ matrix.

After the transformation, you simply discard the last coordinate to get back to 3D. As long as the bottom row of the matrix is $[0 \; 0 \; 0 \; 1]$, the output $w$-coordinate will always be 1, so you just take the first three entries.

---

## The 4x4 Homogeneous Transform Matrix

A homogeneous transform $T$ is a $4 \times 4$ matrix with a specific structure:

$$
T = \begin{bmatrix} R & t \\ 0^\top & 1 \end{bmatrix} = \begin{bmatrix} r_{11} & r_{12} & r_{13} & t_x \\ r_{21} & r_{22} & r_{23} & t_y \\ r_{31} & r_{32} & r_{33} & t_z \\ 0 & 0 & 0 & 1 \end{bmatrix}
$$

Here:

- $R$ is a $3 \times 3$ **rotation matrix** occupying the top-left block. It encodes how the object (or coordinate frame) is oriented. A valid rotation matrix satisfies $R^\top R = I$ and $\det(R) = 1$.
- $t = (t_x, t_y, t_z)^\top$ is a $3 \times 1$ **translation vector** in the rightmost column. It encodes how far the origin has shifted along each axis.
- The bottom row is always $[0 \; 0 \; 0 \; 1]$. This is what keeps the transform "rigid" and ensures the $w$-coordinate stays 1 after multiplication.

---

## Step-by-Step: Applying the Transform

Given a transform $T$ and a 3D point $p = (x, y, z)$, here is the full procedure:

**Step 1: Convert to homogeneous coordinates**

Append a 1:

$$
p_h = \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix}
$$

**Step 2: Multiply by the transform matrix**

$$
p'_h = T \cdot p_h = \begin{bmatrix} R & t \\ 0^\top & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \\ 1 \end{bmatrix}
$$

Expanding the multiplication:

$$
p'_h = \begin{bmatrix} r_{11}x + r_{12}y + r_{13}z + t_x \\ r_{21}x + r_{22}y + r_{23}z + t_y \\ r_{31}x + r_{32}y + r_{33}z + t_z \\ 1 \end{bmatrix}
$$

Notice how the top three rows compute $Rp + t$ exactly. The bottom row just gives 1.

**Step 3: Extract the 3D result**

Drop the last coordinate:

$$
p' = \begin{bmatrix} r_{11}x + r_{12}y + r_{13}z + t_x \\ r_{21}x + r_{22}y + r_{23}z + t_y \\ r_{31}x + r_{32}y + r_{33}z + t_z \end{bmatrix}
$$

This is the transformed point in 3D space.

---

## A Concrete Example

Suppose the transform is a pure translation by $(1, 2, 3)$ with no rotation (identity rotation):

$$
T = \begin{bmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & 1 & 3 \\ 0 & 0 & 0 & 1 \end{bmatrix}
$$

Apply it to the origin $(0, 0, 0)$:

$$
T \begin{bmatrix} 0 \\ 0 \\ 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 + 0 + 0 + 1 \\ 0 + 0 + 0 + 2 \\ 0 + 0 + 0 + 3 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \\ 3 \\ 1 \end{bmatrix}
$$

The result is $(1, 2, 3)$, which is exactly what a translation by $(1, 2, 3)$ should do to the origin.

Now consider a 90-degree rotation around the z-axis combined with a translation of $(1, 0, 0)$:

$$
T = \begin{bmatrix} 0 & -1 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}
$$

Apply to point $(1, 0, 0)$:

$$
T \begin{bmatrix} 1 \\ 0 \\ 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \cdot 1 + (-1) \cdot 0 + 0 \cdot 0 + 1 \\ 1 \cdot 1 + 0 \cdot 0 + 0 \cdot 0 + 0 \\ 0 \cdot 1 + 0 \cdot 0 + 1 \cdot 0 + 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \\ 0 \\ 1 \end{bmatrix}
$$

The point was first rotated ($(1,0,0)$ becomes $(0,1,0)$ under 90-degree z-rotation) and then translated by $(1,0,0)$, giving $(1, 1, 0)$.

---

## Understanding the Rotation Matrix

The $3 \times 3$ rotation matrix $R$ inside $T$ deserves a closer look.

**Rotation around the z-axis by angle $\theta$:**

$$
R_z(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$

**Rotation around the x-axis by angle $\theta$:**

$$
R_x(\theta) = \begin{bmatrix} 1 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta \\ 0 & \sin\theta & \cos\theta \end{bmatrix}
$$

**Rotation around the y-axis by angle $\theta$:**

$$
R_y(\theta) = \begin{bmatrix} \cos\theta & 0 & \sin\theta \\ 0 & 1 & 0 \\ -\sin\theta & 0 & \cos\theta \end{bmatrix}
$$

Key properties of rotation matrices:

- They are **orthogonal**: $R^\top R = I$, meaning the inverse equals the transpose.
- They have **determinant 1**, which distinguishes proper rotations from reflections.
- They **preserve distances**: the length of any vector does not change after rotation.

---

## Composing Multiple Transforms

One of the biggest advantages of homogeneous transforms is that chaining multiple transformations is just matrix multiplication. If you want to first apply $T_1$, then $T_2$, the combined transform is:

$$
T_{\text{combined}} = T_2 \cdot T_1
$$

Note the order: $T_1$ is applied first but appears on the right. This is standard matrix multiplication convention. For a point $p$:

$$
p' = T_2 \cdot (T_1 \cdot p_h) = (T_2 \cdot T_1) \cdot p_h
$$

This lets you stack as many transforms as you need. In robotics, for instance, a robot arm with 6 joints has 6 transforms chained together to compute where the end-effector is in world coordinates:

$$
T_{\text{world}} = T_1 \cdot T_2 \cdot T_3 \cdot T_4 \cdot T_5 \cdot T_6
$$

---

## The Inverse Transform

Given a homogeneous transform $T$, its inverse undoes the operation. For a rigid-body transform, the inverse has a nice closed form:

$$
T^{-1} = \begin{bmatrix} R^\top & -R^\top t \\ 0^\top & 1 \end{bmatrix}
$$

This works because $R$ is orthogonal, so $R^{-1} = R^\top$. The inverse first "un-translates" by $-R^\top t$ and then "un-rotates" by $R^\top$. You do not need a general-purpose matrix inverse for this.

---

## Where Homogeneous Transforms Show Up

**Robotics**: Every joint in a robot arm defines a local coordinate frame. The transform from one joint to the next is a $4 \times 4$ matrix. Forward kinematics chains these together to find the position of the robot's hand relative to its base.

**Computer Graphics**: The rendering pipeline applies a sequence of transforms: model transform (place object in the world), view transform (orient the camera), and projection transform (project onto the screen). Each is a $4 \times 4$ matrix, and they are multiplied together into a single Model-View-Projection (MVP) matrix.

**Computer Vision**: Camera extrinsic parameters are represented as a homogeneous transform that maps points from world coordinates into camera coordinates. This is used in 3D reconstruction, SLAM (Simultaneous Localization and Mapping), and augmented reality.

**Physics Simulations**: Rigid body dynamics track the position and orientation of objects over time. Each object's pose at any instant is a homogeneous transform.